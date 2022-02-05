#!/usr/bin/env python
# coding: utf-8

# # Historical Figures

# In[61]:


import pandas as pd
hf = pd.read_csv("HistoricalFigures_Cleaned.csv")


# 1. Chief Joseph

# In[62]:


hf_Chief = hf[hf["Word Mark"] == "CHIEF JOSEPH"]
hf_Chief


# 7 -> 0
# There are no word marks and international classes for Sitting Bull from this dataset.
# 
# Chief Joseph(1840-1904) refers to a tribe leader of the Nez Perce located in Oregon, and he tried to lead his tribe followers to escape to Canada.

# 2. Cochise

# In[84]:


hf_Cochise = hf[hf["Word Mark"] == "COCHISE"]
hf_Cochise


# In[85]:


hf_Cochise.iloc[:,[9,34]]


# In[86]:


hf_Cochise.iloc[:,[9]].value_counts()


# In[87]:


hf_Cochise.iloc[:,[34]].value_counts()


# 15 --> 8, 
# There are 8 marks for Cochise owned by a federally recognized tribe.
# 
# There is no "key owner" of a mark, since each of the mark is owned by different owners. 
# 
# The most common IC class for the term is IC 025 which owns 3 marks out of 8 marks. 
# 
# The key product class associated with IC 025 is clothing including jeas, jackets, and belts made of leather.
# 
# Cochise was a chief of a tribe called "Chiricahua Apache" located in Arizona territory, and led his followers to resist to White men in the US Southwest in the 1860s. 

# 3. Sitting Bull

# In[88]:


hf_sit = hf[hf["Word Mark"] == "SITTING BULL"]
hf_sit


# 5 --> 0, 
# There are no word marks and international classes for Sitting Bull from this dataset.
# 
# Sitting Bull was a chief leader of Sioux tribe located in South Dakota(midwestern US state). He united Sioux peoples united in their struggle for survival on the North American Great Plains and resist to white men.

# 4. Hiawatha

# In[66]:


hf_hia = hf[hf["Word Mark"] == "HIAWATHA"]
hf_hia


# In[67]:


hf_hia.iloc[:,[9,34]]


# In[73]:


hf_hia.iloc[:,[9]].value_counts()


# In[74]:


hf_hia.iloc[:,[34]].value_counts()


# 49 --> 24, 
# There are 24 marks for Hiawatha owned by a federally recognized tribe.
# 
# There is a "key owner" of a mark, Legends of the West, which owns 6 marks out of 24 marks.
# 
# The most common IC classes for the term are IC 018 and IC 028 which owns 3 marks out of 8 marks each. 
# 
# The key products associated with IC 018 are products all made of leather or immitation leather. The key products associated with IC 028 are dolls, toys, and action figures. 
# 
# Hiawatha was a leader of the Onondaga tribe located in the New York state, contributing to a formation of Iroquois Confederacy. He taught his followers agriculture, navigation, medicine, and the arts, conquering by his magic all the powers of nature that war against man.

# 5. Powhatan

# In[29]:


hf_pow = hf[hf["Word Mark"] == "POWHATAN"]
hf_pow


# In[68]:


hf_pow.iloc[:,[9,34]]


# In[75]:


hf_pow.iloc[:,[9]].value_counts()


# In[76]:


hf_pow.iloc[:,[34]].value_counts()


# 12 --> 6, 
# There are 6 marks for Powhatan owned by a federally recognized tribe. 
# 
# There is no "key owner" of a mark, since those are owned by different owners each.
# 
# The most common IC class for the term is IC 029 which owns 3 marks out of 6 marks. 
# 
# The key product class associated with IC 029 is canned fruits, vegetables, dressings, and syrups.
# 
# Powhatan was a leader of the Powhatan, an alliance of Algonquian-speaking American Indians living in a state of  Virginia.
