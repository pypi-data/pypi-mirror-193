#!/usr/bin/env python
# coding: utf-8

# # How to use `tpmap`
# 
# This notebook demonstrates how to use `tpmap` and other miscelleneous utility functions supporting `pmap`.

# ## Preamble: Install prerequisites, import modules.

# In[1]:


get_ipython().system('pip -q install --upgrade pip')
get_ipython().system('pip -q install --upgrade "jax[cpu]"')
get_ipython().system('pip -q install git+https://github.com/yotarok/bobbin.git')


# In[2]:


get_ipython().run_cell_magic('capture', '', 'import functools\n\nimport bobbin\nimport chex\nimport flax\nimport jax\nimport jax.experimental.host_callback as hcb\nimport jax.numpy as jnp\nimport numpy as np\n\nArray = chex.Array\n# Simulate multi-device environment by CPU\nchex.set_n_cpu_devices(8)\n')


# ## `tpmap`
# 
# `tpmap` is a thin-wrapper for pmap that attaches argument and return-value processings for ensuring transparent API.
# Basically, `tpmap` introduces some mechanism to inject argument translators and a return value translator to `jax.pmap` so `pmap`-ed function doesn't change their input/ output shapes.
# There's additional information needed because normal python functions do not know whether an argument is a data array that should be split, or a parameter array that should be distributed to all the devices.
# `tpmap` provides easier supports for this kind of parameter/ return-value translation.
# 
# Let's first define the function to be parallelized.  The function below performs matrix multiplication and adds some noise to the results.

# In[3]:


def data_parallel_noisy_matmul(matrix, xs, rng):
    noise = 0.1 * jax.random.normal(rng, shape=(1, matrix.shape[-1]))
    device_id = jax.lax.axis_index("i")
    hcb.id_print(device_id, shape_of_parameter=matrix.shape, shape_of_data=xs.shape)
    return jnp.dot(xs, matrix) + noise


# Note that there's some `hcb.*` calls for debugging purpose.
# 
# The function can be transformed into data-parallel function by applying `tpmap` operator as follows:

# In[4]:


f = bobbin.tpmap(
    data_parallel_noisy_matmul,
    axis_name="i",
    argtypes=("broadcast", "shard", "rng"),
    wrap_return=lambda x: x.reshape((-1, x.shape[-1])),
)


# Here, the `argtypes` specifies how to distribute the arguments. Each value has the following instructions.
# 
# - "broadcast": Copy the argument to all the devices involved.
# - "shard": Split the leading axis (batch) by the number of devices and pass each shard to each device.
# - "rng": Split the RNG given as the argument to N child-RNGs and distribute child RNG to each device.
# 
# In addition to the above used values, the following options can be used:
# 
# - "thru": The argument is expected to have a device-axis so the argument is directly passed to the `pmap`-ed function.
# - "static": The argument is assumed to be a static argument that will be broadcasted.
# 
# Furthermore, the method to handle return values is specified as `wrap_return` argument.  In this case, each device returns `(batch_size // device_count, output_dim)`-shaped array, and the default return shape of this function is `(device_count, batch_size // device_count, output_dim)`.  `wrap_return` argument specified above reshapes it back to `(batch_size, output_dim)` so we can ensure the same shape information as the original function.
# 
# By calling `tpmap`-ed function as below, you will see that each function call is performed on a different device, and getting only a part of data.

# In[5]:


batch_size = 16
input_dim = 8
output_dim = 5

parameter = np.random.normal(size=(input_dim, output_dim))
data = np.random.normal(size=(batch_size, input_dim))
result = f(parameter, data, jax.random.PRNGKey(0))
print(f"Result shape = {result.shape}")


# ## Miscelleneous pmap utilities
# 
# Besides `tpmap`, bobbin introduces some convenient tools around pmap.
# 
# ### `unshard`
# 
# `unshard` is useful when to switch from JIT-ed multi-device operation to pure-Python CPU (and single-host) operation.
# The following example does dice rolling on each device and gathers counts as a result.

# In[6]:


class Result(flax.struct.PyTreeNode):
    roll_count: Array
    six_count: Array


@functools.partial(bobbin.tpmap, axis_name="d", argtypes=("static", "rng"))
def roll_dice(count, rng):
    value = jax.random.randint(rng, shape=(count,), minval=1, maxval=7)
    return Result(
        six_count=(value == 6).astype(np.float32).sum(), roll_count=jnp.full((), count)
    )


results = roll_dice(10, jax.random.PRNGKey(0))
results


# Since we didn't set `wrap_return`, the result is a raw sharded representation from `pmap` that has a leading axis corresponding to each device.
# `unshard` is useful for such pytrees, if we want to do separate processing for each shard as follows:

# In[7]:


def print_result(device_id, result):
    six_rate = result.six_count / result.roll_count
    if six_rate > 0.3:
        print(f"Device #{device_id} was lucky! six-rate={six_rate*100:2.0f}%!!")
    else:
        print(f"Device #{device_id} is normal.")


for device_id, result in enumerate(bobbin.unshard(results)):
    print_result(device_id, result)


# ### `gather_from_jax_processes`
# 
# `gather_from_jax_processes` are important in multi-process environment.  In multi-process environment, sometimes one want to gather some metrics.
# In JIT-ed function, this is done by `allgather`.  `gather_from_jax_processes` is a short-cut for performing the similar operations in pure-python context
# (by essentially create a function that only does `allgather` and call it in a `pmap` context.)
# 
# ### `assert_replica_integrity`
# 
# Similar to `gather_from_jax_processes` this is a short cut for checking integrity of the variables that are expected to be identical among the devices.
# This function essentially does `gather_from_jax_processes` on CPU backend, and compare the values from different devices and different processes, and raises an exception if there's mismatch.
# This operation is slow and should only be needed for debugging purpose.
