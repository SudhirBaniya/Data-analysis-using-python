#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Pandas Learning Notebook


# In[5]:


import pandas as pd 
import numpy as np


# In[6]:


df = pd.read_csv(r"C:\Users\urfre\Documents\Sales.csv")


# In[7]:


df


# In[5]:


# Data view using head() and tail()


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.tail(10)


# In[8]:


# Understanding data using describe()


# In[11]:


df.describe


# In[12]:


df.describe(percentiles = [0.3,0.5,0.7])


# In[13]:


df.describe(include = [int])


# In[14]:


df.describe(exclude = [int])


# In[15]:


df.describe().T


# In[14]:


#Quick way to look datatypes, missing values, and data size of the data frame using info()


# In[16]:


df.info()


# In[16]:


# Understanding data using shape()


# In[17]:


df.shape


# In[18]:


df.shape[0]


# In[19]:


df.shape[1]


# In[20]:


#Get all columns and columns name


# In[20]:


df.columns


# In[21]:


list(df.columns)


# In[23]:


# Cheaking for missing values using isnull()


# In[22]:


df.isnull()


# In[25]:


#Lets create missing values


# In[23]:


df2 = df.copy()


# In[24]:


df2.loc[2:5, 'country'] = None


# In[25]:


df2.head(10)


# In[26]:


df2.isnull().head(10)


# In[27]:


df2.isnull().sum()


# In[28]:


df2.isnull().sum().sum()


# In[32]:


# Isolating one rows using[]


# In[29]:


df[df.index==1]


# In[30]:


df[df.index==0]


# In[35]:


# Isolating two or more rows using[]


# In[31]:


df[df.index.isin(range(2,8))]


# In[37]:


# Using .loc[] and .iloc[] to fetch rows


# In[32]:


df2.index = range(0,113036)


# In[33]:


df2.loc[0]


# In[34]:


df2.iloc[0]


# In[35]:


df2.iloc[1]


# In[36]:


df2.loc[1000:1005]


# In[37]:


df.iloc[1000:1005]


# In[38]:


df2.loc[[1000,2000,3000]]


# In[39]:


df2.iloc[[1000,2000,3000]]


# In[40]:


df2.loc[1000:1005,['Country', 'Year', 'Product', 'Order_Quantity']]


# In[41]:


df2.iloc[105:110, :5]


# In[42]:


df2.loc[113030:, ['Country', 'Year', 'Product', 'Order_Quantity']]


# In[43]:


df2.iloc[113030:, : 5]


# In[50]:


# Conditional Slicing


# In[44]:


df[df.Order_Quantity==5]


# In[45]:


df[df.Cost==525]


# In[46]:


df.loc[df['Customer_Age'] > 30,['Country', 'Cost', 'Revenue']]


# In[53]:


#Data cleaning using pandas 


# In[47]:


df2.isnull().sum()


# In[55]:


# Dealing with missing data technique


# In[56]:


# Dropping missing values


# In[48]:


df3 = df2.copy()


# In[49]:


df3 = df3.dropna()


# In[50]:


df3.shape


# In[51]:


df2.shape


# In[52]:


df2.head()


# In[53]:


df3=df2.copy()


# In[54]:


df3.dropna(inplace=True,axis=1)


# In[55]:


df3.head()


# In[56]:


df3=df2.copy()


# In[57]:


df3.dropna(inplace=True,how='all')


# In[58]:


df3.head()


# In[59]:


df2.head()


# In[60]:


df3.dropna(inplace=True,axis=1)


# In[61]:


df3.head()


# In[72]:


# Replacing missing values


# In[62]:


df3=df2.copy()


# In[63]:


mean_value = df3['Profit'].mean()


# In[64]:


df3=df3.fillna(mean_value)


# In[65]:


df3.head()


# In[79]:


# Dealing with Duplicate Data


# In[66]:


df3 = pd.concat([df2,df2])


# In[67]:


df3.shape


# In[68]:


df3 = df3.drop_duplicates()


# In[69]:


df3.shape


# In[102]:


df3.nunique()


# In[77]:


df3.sort_values(by='Revenue', ascending=False).head()


# In[79]:


# Data visualization in pandas 


# In[85]:


df[['Revenue', 'Profit']].plot.line()


# In[86]:


df[['Revenue', 'Profit']].plot.line(figsize=(25,15))


# In[87]:


df.plot.line(subplots=True)


# In[101]:


df.boxplot(figsize=(15,10))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




