#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Auto = pd.read_csv('Auto.csv')
Auto


# In[3]:


import numpy as np


# In[6]:


Auto['mpg']


# In[9]:


np.max(Auto['mpg']), np.min(Auto['mpg'])


# In[10]:


np.max(Auto['displacement']), np.min(Auto['displacement'])


# In[16]:


np.mean(Auto['mpg']), np.std(Auto['mpg'])


# 

# In[14]:


Auto = pd.read_csv('Auto.data',
                  na_values=['?'],
                  delim_whitespace=True)
Auto['horsepower'].sum()


# In[17]:


np.max(Auto['horsepower']), np.min(Auto['horsepower'])


# In[18]:


np.max(Auto['weight']), np.min(Auto['weight'])


# In[19]:


np.max(Auto['acceleration']), np.min(Auto['acceleration'])


# In[20]:


np.mean(Auto['displacement']), np.std(Auto['displacement'])


# In[22]:


np.mean(Auto['weight']), np.std(Auto['weight'])


# In[23]:


np.mean(Auto['acceleration']), np.std(Auto['acceleration'])


# In[24]:


data = Auto.drop(labels=range(10,86), axis=0)


# In[25]:


data


# In[26]:


np.max(data['mpg']), np.min(data['mpg']), np.mean(data['mpg']), np.std(data['mpg'])


# In[27]:


np.max(data['displacement']), np.min(data['displacement']), np.mean(data['displacement']), np.std(data['displacement'])


# In[28]:


np.max(data['horsepower']), np.min(data['horsepower']), np.mean(data['horsepower']), np.std(data['horsepower'])


# In[29]:


np.max(data['weight']), np.min(data['weight']), np.mean(data['weight']), np.std(data['weight'])


# In[30]:


np.max(data['acceleration']), np.min(data['acceleration']), np.mean(data['acceleration']), np.std(data['acceleration'])


# In[34]:


from matplotlib.pyplot import subplots
fig, ax = subplots(figsize=(8,8))
Auto.boxplot('mpg', by='horsepower', ax=ax);


# In[42]:


import matplotlib.pyplot as plt
plt.scatter(Auto['mpg'], Auto['horsepower']);
plt.xlabel("MPG");
plt.ylabel("Horsepower");


# In[43]:


plt.scatter(Auto['mpg'], Auto['displacement']);
plt.xlabel("MPG");
plt.ylabel("Displacement");


# In[44]:


plt.scatter(Auto['mpg'], Auto['weight']);
plt.xlabel("MPG");
plt.ylabel("Weight");


# In[45]:


plt.scatter(Auto['mpg'], Auto['acceleration']);
plt.xlabel("MPG");
plt.ylabel("Acceleration");


# In[46]:


plt.scatter(Auto['displacement'], Auto['horsepower']);
plt.xlabel("Displacement");
plt.ylabel("Horsepower");


# In[47]:


plt.scatter(Auto['weight'], Auto['horsepower']);
plt.xlabel("Weight");
plt.ylabel("Horsepower");


# In[48]:


plt.scatter(Auto['mpg'], Auto['year']);
plt.xlabel("MPG");
plt.ylabel("Year");


# In[49]:


plt.scatter(Auto['mpg'], Auto['cylinders']);
plt.xlabel("MPG");
plt.ylabel("Cylinders");


# In[50]:


plt.scatter(Auto['mpg'], Auto['origin']);
plt.xlabel("MPG");
plt.ylabel("Origin");


# In[ ]:




