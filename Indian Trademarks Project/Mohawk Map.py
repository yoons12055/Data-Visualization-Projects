#!/usr/bin/env python
# coding: utf-8

# # Mohawk Map

# In[2]:


import pandas as pd
df = pd.read_csv('mohawk_cleaned2.csv')
df.head()


# In[3]:


# Using regex with str.extract() with full address
df['Owner']
zip4 = df['Owner'].str.extract(r'(\d{5}\-?\d{0,4})')
df4 = df.loc[:,['Serial Number', 'Owner']]
df4['Zip'] = zip4
df4


# In[4]:


# Save this dataframe as a csv form
df4.to_csv('dfMohawk_csv')


# In[5]:


from IPython.display import Image
Image(filename='mohawk-map.png')

