#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("C:\\Users\\Sujit\\Downloads\\stats.csv")


# In[3]:


df


# MEASURE OF CENTRAL TENDENCY

# In[4]:


# Mean Salary
mean1=df['Salary'].mean()
mean1


# In[5]:


# Sum of Salaries
sum1=df['Salary'].sum()
sum1


# In[6]:


# Maximum Salary
max1=df['Salary'].max()
max1


# In[7]:


# Minimum Salary
min1=df['Salary'].min()
min1


# In[8]:


# Total Count
count1=df['Salary'].count()
count1


# In[9]:


# Median
median=df['Salary'].median()
median


# In[10]:


# Mode
mode1=df['Salary'].mode()
mode1


# In[11]:


countrywise_sum=df.groupby(['Country']).sum()
countrywise_sum


# In[12]:


countrywise_count=df.groupby(['Country']).count()
countrywise_count


# MEASURE OF VARIABILITY

# In[13]:


# Variance of salaries
var1=df['Salary'].var()
var1


# In[14]:


# Standard deviation
std1=df['Salary'].std()
std1


# MEASURE OF SYMMETRY

# In[15]:


skew1=df.skew(axis=0, skipna=True)
skew1


# In[16]:


# The Skewness is positive so x will have right side tail.


# # COVARIANCE AND CORRELATION

# In[18]:


import pandas as pd
bw = pd.read_csv("C:\\Users\\Sujit\\Downloads\\BirthWeight.csv")
bw.head()


# In[19]:


bw.set_index('Infant ID', inplace=True)
bw.head()


# In[20]:


bw.cov()


# In[21]:


bw.corr(method="pearson")


# In[22]:


# Covariance indicates that there is correlation exists between two Correlation coefficient of 0.818 indicates the relation between two variable is strong. 


# In[23]:


#importing required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
from scipy.stats import kurtosis


# In[24]:


pd.set_option("display.max_columns",None)
pd.options.display.float_format = "{:,.2f}".format


# Format : A data frame with 53940 rows and 10 variables
# 
# Description : A dataset containing the prices and other attributes of almost 54,000 diamonds.
# 
# The variables are as follows:
# 
# price: price in US dollars ( 326−− 18,823) carat: weight of the diamond (0.2--5.01) cut: quality of the cut (Fair, Good, Very Good, Premium, Ideal) colour: diamond colour, from J (worst) to D (best) clarity: a measurement of how clear the diamond is (IF (best), VVS1, VVS2, VS1, VS2, SI1, SI2, I1 (worst) ) popularity: popularity of this specs (Good, Fair, Poor) x: length in mm (0--10.74) y: width in mm (0--58.9) z: depth in mm (0--31.8) depth: total depth percentage = z / mean(x,y) = 2 * z /(x+y) (43--79) table: width of top of diamondrelative to widest point (43--95)

# In[25]:


# reading data from csv file
xls = pd.read_csv("C:\\Users\\Sujit\\Downloads\\diamonds.csv")
xls.head()


# In[26]:


des_df = xls.drop(['id'],axis= 1) #drop id colums
for col in des_df:            #drop all alpha-numeric colms
    if des_df[col].dtype =='object':
        des_df = des_df.drop([col],axis = 1)
        
des_r = des_df.describe()
des_df = des_r.rename(index={'50%':'median/50%'})
des_r


# In[27]:


var_r = des_df.var() #Calculating variance seperately

varlist = []
for col in des_df.columns:
    if des_df[col].dtype == 'object':
        continue
    varlist.append(round(des_df[col],5))

df = pd.DataFrame([varlist],columns=des_r.columns,index=['var'])
mct = des_r.append(df) #Adding var to describe result
mct


# In[ ]:




