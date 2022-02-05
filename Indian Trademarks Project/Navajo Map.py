#!/usr/bin/env python
# coding: utf-8

# # Navajo Map

# In[1]:


import pandas as pd
df = pd.read_csv('navajo_cleaned_combined.csv')
df.head()


# In[2]:


# Using regex with str.extract() with full address
df['Owner']
zip5 = df['Owner'].str.extract(r'(\d{5}\-?\d{0,4})')
df5 = df.loc[:,['Serial Number', 'Owner']]
df5['Zip'] = zip5
df5


# In[3]:


# Save this dataframe as a csv form
df5.to_csv('dfNavajo_csv')


# In[4]:


from IPython.display import Image
Image(filename='navajo-map.png')

