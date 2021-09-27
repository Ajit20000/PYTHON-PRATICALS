#!/usr/bin/env python
# coding: utf-8

# # SEABORN

# • Seaborn is a Python data visualization library based on matplotlib • It provides a high level interface for drawing attractive and informative statistical graphics

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[7]:


os.chdir('C:\\Users\\Sujit\\Desktop\\anita mam')
cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
cars_data.size


# In[8]:


cars_data.dropna(axis=0,inplace=True)
cars_data.size


# In[9]:


cars_data=pd.read_csv('Toyota.csv',index_col=0)
cars_data.head()


# In[10]:


sns.set(style="darkgrid")
sns.regplot(x=cars_data['Age'],y=cars_data['Price'])


# #Scatter plot of Price vs Age without the regression fit line

# In[11]:


sns.regplot(x=cars_data['Age'],y=cars_data['Price'],fit_reg=False)


# In[16]:


sns.regplot(x=cars_data['Age'],y=cars_data['Price'],marker="*",fit_reg=False)


# In[17]:


sns.lmplot(x='Age',y='Price' , data=cars_data,fit_reg=False , hue='FuelType',legend=True,palette="Set1")


# In[22]:


sns.distplot(cars_data['Age'])


# In[23]:


sns.distplot(cars_data['Age'],kde=False)


# In[24]:


sns.distplot(cars_data['Age'],kde=False,bins=5)


# In[25]:


sns.countplot(x="FuelType", data=cars_data)


# In[26]:


sns.countplot(x="FuelType", data=cars_data, hue="Automatic")


# In[27]:


sns.boxplot(x=cars_data['FuelType'],y=cars_data['Price'])


# In[28]:


sns.pairplot(cars_data,kind="scatter",hue="FuelType",diag_kws={'bw': 0.1})
plt.show()


# In[ ]:




