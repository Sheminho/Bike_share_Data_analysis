#!/usr/bin/env python
# coding: utf-8

# # importing

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from datetime import datetime


# # Data Wrangling
# ## Data Gathering

# In[2]:


df_chic = pd.read_csv('chicago.csv')
df_ny = pd.read_csv('nyc.csv')
df_wash = pd.read_csv('washington.csv')


# ## Data Assessing

# In[3]:


df_chic.head()


# In[4]:


df_ny.head()


# In[5]:


df_wash.head()


# In[6]:


df_chic.info()


# In[7]:


df_ny.info()


# In[8]:


df_wash.info()


# In[9]:


df_chic.duplicated().sum()


# In[10]:


df_ny.duplicated().sum()


# In[11]:


df_wash.duplicated().sum()


# ## Data Cleaning

# In[12]:


df_chic.dropna(inplace=True)


# In[13]:


df_ny.dropna(inplace=True)


# In[14]:


df_chic['Start Time'] = pd.to_datetime(df_chic['Start Time'])
df_chic['End Time'] = pd.to_datetime(df_chic['End Time'])
df_ny['End Time'] = pd.to_datetime(df_ny['End Time'])
df_ny['Start Time'] = pd.to_datetime(df_ny['Start Time'])
df_wash['Start Time'] = pd.to_datetime(df_wash['Start Time'])
df_wash['End Time'] = pd.to_datetime(df_wash['End Time'])


# In[15]:


df_chic['State'] = 'Chicago'
df_ny['State'] = 'New York'
df_wash['State'] = 'washington'


# In[16]:


df_chic['Birth Year'] = df_chic['Birth Year'].astype(int)
df_ny['Birth Year'] = df_ny['Birth Year'].astype(int)


# In[17]:


df = df_chic


# In[18]:


df = df.append(df_ny)


# In[19]:


df = df.append(df_wash)


# In[20]:


df.info()


# In[21]:


df.head()


# # Data Exploration, Mining

# In[22]:


df['Start Station'].value_counts()


# In[23]:


df['End Station'].value_counts()


# In[24]:


df['Start Time'].mode()


# In[25]:


df['State'].value_counts()


# In[26]:


plt.hist(df.State)


# In[110]:


plt.scatter(df["Start Time"], df["Trip Duration"])


# In[111]:


df.to_csv('BikeShare_Mod.csv')

