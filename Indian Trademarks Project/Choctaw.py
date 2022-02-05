#!/usr/bin/env python
# coding: utf-8

# # Choctaw Data Cleaning 

# In[3]:


import pandas as pd
data = pd.read_excel('Choctaw.xlsx')
choc = pd.DataFrame(data)
choc


# In[4]:


choc.columns


# In[5]:


choc = choc.rename(columns={'Unnamed: 0':"A",
                        'Unnamed: 1':"B",
                        'Unnamed: 2':"C",
                        'Unnamed: 3':"D",
                        'Unnamed: 4':"E",
                        'Unnamed: 5':"F"})
choc


# In[6]:


choc = choc[choc['B']!= "List At:"]
choc


# In[7]:


choc.A.unique()


# In[8]:


choc = choc[choc['A']!= "Home|Site Index|Search|FAQ|Glossary|Contacts|eBusiness|eBiz alerts|News"]
choc = choc[choc['A']!= "Trademarks >\n      Trademark Electronic Search System (TESS)"]
choc


# In[9]:


choc = choc[["A", "B"]]
choc = choc.dropna(subset=["A"])
choc.head(20)


# In[10]:


choc = choc.reset_index(drop=True)
choc


# In[13]:


choc1 = choc[choc['A'] == 'TESS was last updated on Mon Apr 19 03:47:23 EDT 2021']
a = list(choc1.index.values)
l = a[1:]
l_mod = [0] + l + [max(l) + 1]
list_of_dfs = [choc.iloc[l_mod[n]:l_mod[n+1]] for n in range(len(l_mod)-1)]
list_of_dfs[0]


# In[14]:


list_of_dfs_adjusted = [i.T for i in list_of_dfs]
list_of_dfs_adjusted[0]


# In[15]:


for i in range(len(list_of_dfs_adjusted)):
    new_header = list_of_dfs_adjusted[i].iloc[0] 
    list_of_dfs_adjusted[i] = list_of_dfs_adjusted[i][1:] 
    list_of_dfs_adjusted[i].columns = new_header
list_of_dfs_adjusted[0]


# In[17]:


import numpy as np
list_of_dfs_adj = pd.DataFrame([np.repeat([1],32)], columns=list(choc.A.unique()))
for i in list_of_dfs_adjusted:
    list_of_dfs_adj = list_of_dfs_adj.append(i)
list_of_dfs_adj = list_of_dfs_adj.iloc[1:]
list_of_dfs_adj


# In[18]:


list_of_dfs_adj.columns


# In[19]:


choc_final = list_of_dfs_adj.drop(['TESS was last updated on Mon Apr 19 03:47:23 EDT 2021',
                                  '|.HOME | SITE INDEX| SEARCH \n   | eBUSINESS\n    | HELP | PRIVACY POLICY'], axis = 1)
choc_final


# In[20]:


choc_final = choc_final.reset_index(drop = True)
choc_final = choc_final.dropna(axis = 0, subset = ['Word Mark'])
choc_final


# In[21]:


#Create US code column
def us_code(df):
    df['US code'] = df['Goods and Services'].str.extract(r'(US\s.*?\.)')
    df['US code'] = df['US code'].fillna('')
    df['US code'] = df['US code'].str.strip('US.').str.split()
    df = df.groupby("Serial Number").first() # the reason why duplicates get cut
    return df


# In[22]:


choc_final = us_code(choc_final)
choc_final.head()


# In[23]:


choc_final['International Class (IC)'] = choc_final['Goods and Services'][choc_final['Goods and Services'] != "IC 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 200 A B . US 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 046 047 048 049 050 051 052 100 101 102 103 104 105 106 107 200 A B . G & S: NO GOODS/SERVICES STATEMENT ON TRAM"]
choc_final[['International Class (IC)']]


# In[24]:


choc_final['International Class (IC)'] = choc_final['International Class (IC)'].str.extract(r'(IC\s+\d{3})')
choc_final


# In[26]:


choc_final["Year"] = choc_final["Filing Date"].str[-4:]
choc_final['Year'].unique()
choc_final[choc_final['Year'] == '0000']
choc_final


# In[29]:


tst = choc_final.copy()


# In[35]:


#Create US code column
def design_code(df):
    df['Design Search Code (extracted)'] = df['Design Search Code'].str.findall(r'\d+.\d+.\d+')
    df['Design Search Code (extracted)'] = df['Design Search Code (extracted)'].fillna(0)
    return df


# In[36]:


tst = design_code(tst)
tst['Design Search Code (extracted)']


# In[37]:


choc_final = design_code(choc_final)
choc_final['Design Search Code (extracted)']


# In[38]:


choc_final


# In[39]:


choc_final.to_csv("Choctaw_cleaned.csv")

