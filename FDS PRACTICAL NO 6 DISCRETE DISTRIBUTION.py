#!/usr/bin/env python
# coding: utf-8

# # IMPORTING DATATYPES

# In[1]:


#for inline plots in jupyter
get_ipython().run_line_magic('matplotlib', 'inline')
#import matplotlib
import matplotlib.pyplot as plt
#for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
import numpy as np


# In[2]:


#import seaborn
import seaborn as sns
#setting for seaborn plotting style
sns.set(color_codes=True)
#settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})


# # UNIFORM DISTRIBUTION

# In[3]:


from scipy.stats import randint
import matplotlib.pyplot as plt
fig,ax = plt.subplots(1,1)

#Calculate a few first moments:

low, high = 7,31
mean, var, skew, kurt = randint.stats(low, high, moments="mvsk")


#Display the probability mas function (''pmf''):

x= np.arange(randint.ppf(0.01,low, high), randint.ppf(0.99,low, high))
ax.plot(x, randint.pmf(x, low, high), 'bo', ms=8, label='randint pmf')
ax.vlines(x, 0, randint.pmf(x, low, high), colors='b', lw=5 ,alpha=0.5)


# In[4]:


x


# In[5]:


prob=randint.cdf(x,low,high)
prob


# # BERNOULLI DISTRIBUTION

# In[6]:


from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size=10000,p=0.6)


# In[7]:


ax=sns.distplot(data_bern,
              kde=False,
              color="skyblue",
              hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')


# # BINOMIAL DISTRIBUTION

# In[8]:


from scipy.stats import binom
data_binom=binom.rvs(n=10,p=0.8,size=10000)


# In[11]:


ax=sns.distplot(data_binom,
              kde=False,
              color="skyblue",
              hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')


# # POISSION DISTRIBUTION

# In[12]:


from scipy.stats import poisson
data_poisson = poisson.rvs(mu=3, size=10000)


# In[13]:


ax=sns.distplot(data_poisson,
              kde=False,
              color="skyblue",
              hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')


# In[ ]:




