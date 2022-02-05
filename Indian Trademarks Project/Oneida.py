#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning for Oneida Tribe

# In[3]:


import pandas as pd
data = pd.read_excel('Oneida.xlsx')
onei = pd.DataFrame(data)
onei


# In[6]:


onei = onei.rename(columns={'Column 1':"A",
                        'Column 2':"B",
                        'Column 3':"C",
                        'Column 4':"D",
                        'Column 5':"E",
                        'Column 6':"F"})
onei = onei[onei['B']!= "List At:"]
onei


# In[7]:


onei.A.unique()


# In[8]:


onei = onei[onei['A']!= "Home|Site Index|Search|FAQ|Glossary|Contacts|eBusiness|eBiz alerts|News"]
onei = onei[onei['A']!= "Trademarks >\n      Trademark Electronic Search System (TESS)"]
onei


# In[10]:


onei = onei[["A", "B"]]
onei = onei.dropna(subset=["A"])
onei = onei.reset_index(drop=True)
onei


# In[11]:


onei1 = onei[onei['A'] == 'TESS was last updated on Mon Apr 19 03:47:23 EDT 2021']
a = list(onei1.index.values)
l = a[1:]
l_mod = [0] + l + [max(l) + 1]
list_of_dfs = [onei.iloc[l_mod[n]:l_mod[n+1]] for n in range(len(l_mod)-1)]
list_of_dfs[0]


# In[12]:


list_of_dfs_adjusted = [i.T for i in list_of_dfs]
list_of_dfs_adjusted[0]


# In[13]:


for i in range(len(list_of_dfs_adjusted)):
    new_header = list_of_dfs_adjusted[i].iloc[0] 
    list_of_dfs_adjusted[i] = list_of_dfs_adjusted[i][1:] 
    list_of_dfs_adjusted[i].columns = new_header 
list_of_dfs_adjusted[0]


# In[15]:


import numpy as np
list_of_dfs_adj = pd.DataFrame([np.repeat([1],31)], columns=list(onei.A.unique()))
for i in list_of_dfs_adjusted:
    list_of_dfs_adj = list_of_dfs_adj.append(i)
list_of_dfs_adj = list_of_dfs_adj.iloc[1:]
list_of_dfs_adj


# In[16]:


list_of_dfs_adj.columns


# In[18]:


onei_final = list_of_dfs_adj.drop(['TESS was last updated on Mon Apr 19 03:47:23 EDT 2021',
                                  '|.HOME | SITE INDEX| SEARCH \n   | eBUSINESS\n    | HELP | PRIVACY POLICY'], axis = 1)
onei_final = onei_final.reset_index(drop = True)
onei_final


# In[19]:


def us_code(df):
    df['US code'] = df['Goods and Services'].str.extract(r'(US\s.*?\.)')
    df['US code'] = df['US code'].fillna('')
    df['US code'] = df['US code'].str.strip('US.').str.split()
    df = df.groupby("Serial Number").first() # the reason why duplicates get cut
    return df


# In[20]:


onei_final = us_code(onei_final)
onei_final.head()


# In[23]:


onei_final['International Class (IC)'] = onei_final['Goods and Services'][onei_final['Goods and Services'] != "IC 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 200 A B . US 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 046 047 048 049 050 051 052 100 101 102 103 104 105 106 107 200 A B . G & S: NO GOODS/SERVICES STATEMENT ON TRAM"]
onei_final['International Class (IC)'] = onei_final['International Class (IC)'].str.extract(r'(IC\s+\d{3})')
onei_final[['International Class (IC)']]


# In[24]:


onei_final["Year"] = onei_final["Filing Date"].str[-4:]
onei_final


# In[25]:


onei_final['Year'].unique()


# In[26]:


onei_final[onei_final['Year'] == '0000']


# In[27]:


tst = onei_final.copy()


# In[30]:


#Create US code column
def design_code(df):
    df['Design Search Code (extracted)'] = df['Design Search Code'].str.findall(r'\d+.\d+.\d+')
    df['Design Search Code (extracted)'] = df['Design Search Code (extracted)'].fillna(0)
    return df


# In[31]:


tst = design_code(tst)
tst['Design Search Code (extracted)']


# In[32]:


onei_final = design_code(onei_final)
onei_final['Design Search Code (extracted)']


# In[33]:


onei_final


# In[35]:


onei_final.to_csv("Oneida_cleaned.csv")

