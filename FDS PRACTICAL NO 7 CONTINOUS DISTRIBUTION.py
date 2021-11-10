#!/usr/bin/env python
# coding: utf-8

# # IMPORTING DATATYPES

# In[1]:


# for inline plots in jupyter
get_ipython().run_line_magic('matplotlib', 'inline')
# import matplotlib
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
import numpy as np


# In[2]:


# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# setting for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})


# # UNIFORM DISTRIBUTION

# In[3]:


# Import uniform distribution
from scipy.stats import uniform


# In[4]:


# random numbers from uniform distribution
n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size = n, loc = start, scale= width)


# In[5]:


ax = sns.distplot(data_uniform,
                 bins=100,
                 kde=True,
                 color='skyblue',
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Uniform Distribution', ylabel='Frequency')


# # NORMAL DISTRIBUTION

# In[6]:


from scipy.stats import norm
# generate random numbers from N(0,1)
data_normal = norm.rvs(size=10000,loc=0,scale=1)


# In[7]:


ax = sns.distplot(data_normal,
                 bins=100,
                 kde=True,
                 color='skyblue',
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')


# # EXPONENTIAL DISTRIBUTION

# In[8]:


from scipy.stats import expon
data_expon = expon.rvs(scale=1,loc=0,size=1000)


# In[9]:


ax = sns.distplot(data_expon,
                bins=100,
                kde=True,
                color="skyblue",
                hist_kws={"linewidth":15,"alpha":1})
ax.set(xlabel='Exponential Distribution',ylabel='Frequency')


# # CHI SQUARE DISTRIBUTION

# In[10]:


from numpy import random

x = random.chisquare(df=2, size=(2,3))

print(x)


# In[11]:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()


# # WEIBULL DISTRIBUTION

# In[12]:


a = 5. # shape

s = np.random.weibull(a,1000)


# In[13]:


import matplotlib.pyplot as plt

x=np.arange(1,100.)/50.

def weib(x,n,a):
    
    return (a/n) * (x/n)**(a-1) * np.exp(-(x/n)**a)


# In[14]:


count, bins, ignored = plt.hist(np.random.weibull(5.,1000))

x=np.arange(1,100.)/50.

scale = count.max()/weib(x, 1., 5.).max()

plt.plot(x,weib(x, 1., 5.)*scale)

plt.show()


# In[ ]:




