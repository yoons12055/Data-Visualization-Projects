#!/usr/bin/env python
# coding: utf-8

# # Cherokee Map

# In[67]:


import pandas as pd
df = pd.read_csv('cherokee_cleaned2.csv')
df.head()


# In[68]:


# Full Address listed 
df['Owner']


# In[69]:


# Using regex with str.extract()
zip1 = df['Owner'].str.extract(r'(\d{5}\-?\d{0,4})')
df1 = df.loc[:,['Serial Number', 'Owner']]
df1['Zip'] = zip1
df1


# In[71]:


# Save this dataframe as a csv form
df1_csv = df1.to_csv()


# In[72]:


from IPython.display import Image
Image(filename='S9z6D-cherokee-map.png') 

