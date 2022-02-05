#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('eskimo_cleaned2.csv')
df.head()


# In[2]:


# Using regex with str.extract() with full address
df['Owner']
zip3 = df['Owner'].str.extract(r'(\d{5}\-?\d{0,4})')
df3 = df.loc[:,['Serial Number', 'Owner']]
df3['Zip'] = zip3
df3


# In[3]:


# Save this dataframe as a csv form
df3.to_csv('dfEskimo_csv', index = False)


# In[4]:


from IPython.display import Image
Image(filename='eskimo-map.png')

