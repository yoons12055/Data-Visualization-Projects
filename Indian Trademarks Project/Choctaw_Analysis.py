#!/usr/bin/env python
# coding: utf-8

# # Choctaw Analysis

# In[2]:


import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
plt.rcParams['figure.figsize'] = (12, 9)


# In[4]:


data = pd.read_csv('Choctaw_cleaned.csv')
choc = pd.DataFrame(data)
choc


# Tribe Ownership
# 
# How many marks are owned by a federally recognized tribe?
# --> 44 marks
# 
# Key Owners --> Choctaw Nation of Oklahoma Federally Recognized Indian Tribe(8), Choctaw Nation of Oklahoma FEDERALLY-RECOGNIZED INDIAN TRIBE(5), Choctaw Defense Munitions(3)

# In[5]:


pd.set_option('display.max_colwidth', None)
choc["Owner"]


# In[6]:


#Create a table of the marks by owner (note: several duplicates due to inconsistent filing)
choc_owners = choc.groupby("Owner").agg(np.size)[["Word Mark"]].sort_values("Word Mark", ascending = False)
choc_owners


# International Class
# 
# What is the most common IC for the term? Is there a key product class with which the term is associated?

# In[7]:


choc["International Class (IC)"]


# In[14]:


choc.loc[55, "International Class (IC)"] = 'IC 040'
choc.loc[56, "International Class (IC)"] = 'IC 040'
choc.loc[57, "International Class (IC)"] = 'IC 042'
choc.loc[58, "International Class (IC)"] = 'IC 042'
choc.loc[64, "International Class (IC)"] = 'IC 013'
choc.loc[65, "International Class (IC)"] = 'IC 013'
choc.loc[66, "International Class (IC)"] = 'IC 013'
choc.loc[69, "International Class (IC)"] = 'IC 035'


# In[15]:


choc_ic = choc.groupby("International Class (IC)").agg(np.size)[["Word Mark"]].sort_values("Word Mark", ascending = False)
choc_ic


# In[16]:


choc_ic.plot.barh()
plt.title("Choctaw: IC Counts", fontsize=20);
plt.ylabel("IC");
plt.xlabel("Number of marks filed");


# The most common classes are 35(Advertising, business management, business administration), 41(Education and Entertainment), and 16(Paper, cardboard and goods made from these materials).

# In[17]:


choc_ic_35 = choc.loc[choc['International Class (IC)'] == 'IC 035']
choc_ic_35


# In[18]:


choc_ic_41 = choc.loc[choc['International Class (IC)'] == 'IC 041']
choc_ic_41


# In[19]:


choc_ic_16 = choc.loc[choc['International Class (IC)'] == 'IC 016']
choc_ic_16

