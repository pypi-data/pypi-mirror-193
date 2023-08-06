#!/usr/bin/env python
# coding: utf-8

# # How to use `var_util` API
# 
# This short notebook demonstrates how to use "var_util" API of Bobbin. "var_util" is aimint at providing an easy way to access to deeply nested pytree structures.

# ## Preamble: Install prerequisites, import modules.

# In[1]:


get_ipython().system('pip -q install --upgrade pip')
get_ipython().system('pip -q install --upgrade "jax[cpu]"')
get_ipython().system('pip -q install git+https://github.com/yotarok/bobbin.git')


# In[2]:


get_ipython().run_cell_magic('capture', '', 'import bobbin\nimport chex\nimport flax\nimport flax.linen as nn\nimport jax\nimport jax.numpy as jnp\nimport numpy as np\n')


# ## Define an array tree via `nn.Module`
# 
# In this notebook, we demonstrate how to inspect/ manipulate the variables in some Flax modules. For this, we define a module that has several parameters, as follows:

# In[3]:


Array = chex.Array


# You can use your custom pytree node as a part of variable.
class DiagnosticInfo(flax.struct.PyTreeNode):
    average_entropy: float
    input_norms: Array


class GaussianClassifier(nn.Module):
    class_count: int = 4

    @nn.compact
    def __call__(self, x):
        *unused_batch_sizes, dims = x.shape
        means = self.param("means", nn.initializers.normal(), (dims, self.class_count))
        logprecs = self.param(
            "logprecs", nn.initializers.zeros_init(), (dims, self.class_count)
        )

        diffs = x[..., np.newaxis] - means.reshape((1,) * (x.ndim - 1) + means.shape)
        diffs = jnp.exp(logprecs.reshape((1,) * (x.ndim - 1) + logprecs.shape)) * diffs
        logits = jnp.sum(-diffs, axis=-2)
        class_logprob = jax.nn.log_softmax(logits)
        avg_entropy = jnp.mean(jnp.sum(-class_logprob * np.exp(class_logprob), axis=-1))
        self.sow(
            "diagnosis",
            "info",
            DiagnosticInfo(
                average_entropy=avg_entropy,
                input_norms=jnp.sqrt(jnp.sum(x * x, axis=-1)),
            ),
        )
        return class_logprob


# The variable tree for this module can be obtained following normal Flax procedure, as follows:

# In[4]:


batch_size = 4
dims = 3
mod = GaussianClassifier()
variables = mod.init(jax.random.PRNGKey(0), np.zeros((batch_size, dims)))


# ## Paths for variables
# 
# "var_util" provides methods to access various pytrees via "path"s.
# Paths are unique identifiers for each nodes in the tree.  Leaves in the tree can be enumerated by using `flatten_with_paths` function as follows:

# In[5]:


list(bobbin.var_util.flatten_with_paths(variables))


# Similarly to obtaining the list of pairs, a path-tree where each node is replaced by its path string can be obtained as follows:

# In[6]:


paths = bobbin.var_util.nested_vars_to_paths(variables)
paths


# Such path-trees are particularly important for doing some path-dependent operations over the tree. The following example overwrites "logprecs" parameters in the tree by ones.

# In[7]:


def reset_logprecs(x, path):
    return jnp.ones_like(x) if path.endswith("logprecs") else x


variables = jax.tree_util.tree_map(reset_logprecs, variables, paths)
variables


# One can also use this mechanism to compute L2 norm for the specific parameters.

# In[8]:


def compute_squared_l2norm_for_logprecs(x, path):
    return jnp.sum(x * x) if path.endswith("logprecs") else 0.0


norm_tree = jax.tree_util.tree_map(
    compute_squared_l2norm_for_logprecs, variables, paths
)
squared_l2_norm = jax.tree_util.tree_reduce(lambda acc, x: acc + x, norm_tree, 0.0)
print(squared_l2_norm)


# ## JSON dumps
# 
# For some use cases, JSON serialization for py-trees are useful, for example, for storing the evaluation results.  Due to the inefficiency of text format, it is not recommended to store whole variables in this way, but some cases like evaluation metrics, that is convenient.
# 
# The JSON format can be obtained via `dump_pytree_json` function used as below:

# In[9]:


json_text = bobbin.var_util.dump_pytree_json(variables)
print(json_text)


# Here, you see that the array is stored with a special marker `"__array__": true`
# and `dtype` field.  However, other than that it is a normal JSON format that you can use various tools for manipulating it.  If you want to write it directly to file systems (or GCS buckets), you may use [`write_pytree_json_file`](https://bobbin.readthedocs.io/en/latest/api.html#bobbin.write_pytree_json_file) instead.
# 
# Loading JSON can be done by [`parse_pytree_json`](https://bobbin.readthedocs.io/en/latest/api.html#bobbin.parse_pytree_json) or it's file-based equivalent, [`read_pytree_json_file`](https://bobbin.readthedocs.io/en/latest/api.html#bobbin.read_pytree_json_file).
# 
# For those functions, you need to specify `template` parameter for specifying the structure of a pytree to be loaded. Here, in the example below, template is obtained by initializing the same flax module (with different RNG key).

# In[10]:


another_vars = mod.init(jax.random.PRNGKey(1), np.zeros((batch_size, dims)))
loaded_vars = bobbin.var_util.parse_pytree_json(json_text, another_vars)
loaded_vars


# It should be noted that `template` argument is only used for obtaining the tree structure, so it will not be altered after calling `parse_pytree_json` (or `read_pytree_json_file`.

# In[11]:


another_vars


# ## Miscelleneous utilities

# [`bobbin.summarize_shape`](https://bobbin.readthedocs.io/en/latest/api.html#bobbin.summarize_shape) can be used for obtaining shapes of the variable tree.

# In[12]:


print(bobbin.summarize_shape(variables))


# Such shape information can be helpful when it is written as the TensorBoard text summary.
# 
# Also, there's a short-cut for obtaining the total number of parameteres.

# In[13]:


print("# of variables =", bobbin.total_dimensionality(variables))


# In[ ]:




