#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st


# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 


# In[16]:


pwd


# In[22]:


data = pd.read_csv('/Users/chakrika/Desktop/OnlineSalesData.csv')


# In[24]:


data.head()


# In[30]:


print(data.columns)


# In[37]:


print(data.isnull().sum())


# In[39]:


df_data = data.dropna()


# In[ ]:




