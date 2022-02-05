#!/usr/bin/env python
# coding: utf-8

# # Apache Tribe Map

# In[23]:


import pandas as pd
df = pd.read_csv('apache_cleaned2.csv')
df.head()


# In[24]:


# Using regex with str.extract() with full address
df['Owner']
zip2 = df['Owner'].str.extract(r'(\d{5}\-?\d{0,4})')
df2 = df.loc[:,['Serial Number', 'Owner']]
df2['Zip'] = zip2
df2


# In[28]:


# Save this dataframe as a csv form
df2.to_csv('dfApache_csv', index=False)


# In[30]:


from IPython.display import Image
Image(filename='apache-map.png')

