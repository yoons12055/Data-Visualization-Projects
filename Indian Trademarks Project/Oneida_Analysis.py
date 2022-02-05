#!/usr/bin/env python
# coding: utf-8

# # Oneida Analysis

# In[2]:


import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
plt.rcParams['figure.figsize'] = (12, 9)
data = pd.read_csv('Oneida_cleaned.csv')
onei = pd.DataFrame(data)
onei


# Tribe Ownership
# 
# How many marks are owned by a federally recognized tribe? --> 14 marks
# 
# Key Owners --> ONEIDA LTD. CORPORATION(5), ONEIDA CONSUMER(5), Oneida Tribe of Indians of Wisconsin SOVEREIGN INDIAN NATION(2)

# In[3]:


pd.set_option('display.max_colwidth', None)
onei["Owner"]


# In[4]:


onei_owners = onei.groupby("Owner").agg(np.size)[["Word Mark"]].sort_values("Word Mark", ascending = False)
onei_owners


# International Class
# 
# What is the most common IC for the term? Is there a key product class with which the term is associated?

# In[5]:


onei["International Class (IC)"]


# In[7]:


onei.loc[24, "International Class (IC)"] = 'IC 014'
onei.loc[44, "International Class (IC)"] = 'IC 003'
onei.loc[56, "International Class (IC)"] = 'IC 035'
onei.loc[59, "International Class (IC)"] = 'IC 006'
onei.loc[60, "International Class (IC)"] = 'IC 006'
onei.loc[67, "International Class (IC)"] = 'IC 041'
onei.loc[77, "International Class (IC)"] = 'IC 041'
onei.loc[79, "International Class (IC)"] = 'IC 035'
onei.loc[84, "International Class (IC)"] = 'IC 041'
onei.loc[85, "International Class (IC)"] = 'IC 016'
onei.loc[90, "International Class (IC)"] = 'IC 041'
onei.loc[91, "International Class (IC)"] = 'IC 009'
onei.loc[92, "International Class (IC)"] = 'IC 008'
onei.loc[93, "International Class (IC)"] = 'IC 008'
onei.loc[94, "International Class (IC)"] = 'IC 037'
onei.loc[95, "International Class (IC)"] = 'IC 001'
onei["International Class (IC)"]


# In[9]:


onei_ic = onei.groupby("International Class (IC)").agg(np.size)[["Word Mark"]].sort_values("Word Mark", ascending = False)
onei_ic


# In[10]:


onei_ic.plot.barh()
plt.title("Oneida: IC Counts", fontsize=20);
plt.ylabel("IC");
plt.xlabel("Number of marks filed");


# The most common classes are 8(Goods or Services), 21(small, hand-operated utensils and apparatus for houshold kitchen use), and 35(Advertising, business management, business administration).

# In[12]:


onei_ic_8 = onei.loc[onei['International Class (IC)'] == 'IC 008']
onei_ic_8


# In[13]:


onei_ic_21 = onei.loc[onei['International Class (IC)'] == 'IC 021']
onei_ic_21


# In[14]:


onei_ic_35 = onei.loc[onei['International Class (IC)'] == 'IC 035']
onei_ic_35

