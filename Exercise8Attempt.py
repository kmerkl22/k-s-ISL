#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
college = pd.read_csv('College.csv')
college


# In[2]:


college2 = pd.read_csv('College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college3.set_index('College')


# In[3]:


college = college3


# In[6]:


college[['Apps','Accept']].describe()


# In[9]:


pd.plotting.scatter_matrix(college[['Top10perc', 'Apps', 'Enroll']]);


# In[11]:


from matplotlib.pyplot import subplots
fig, ax = subplots(figsize=(8, 8))
college.boxplot('Outstate', by='Private', ax=ax);


# In[12]:


college['Elite'] = pd.cut(college['Top10perc'],
                          [0,0.5,1],
                          labels=['No', 'Yes'])


# In[13]:


college.value_counts()


# In[14]:


from matplotlib.pyplot import subplots
fig, ax = subplots(figsize=(8, 8))
college.boxplot('Outstate', by='Elite', ax=ax);


# In[15]:


college.plot.hist()


# In[17]:


fig, ax = plt.subplots(2,2)


# In[ ]:




