import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Jermaine Foskey

# In[10]:


content = pd.read_csv('100 Sales Records.csv')


# In[11]:


content


# In[12]:


type(content)


# In[13]:


content.head(15)


# In[14]:


content.head(2)


# In[15]:


content = content.rename(columns ={'Region': 'Regions'})	


# In[16]:


content.head(2)


# In[17]:


content = content.rename(columns ={'Regions': 'Region'})


# In[18]:


content


# In[19]:


Region = content[content.Region == 'Asia']


# In[20]:


Region


# In[21]:


column = content.Country


# In[22]:


column


# In[23]:


column = content[['Country','Item Type']]


# In[24]:


column


# In[25]:


content


# In[26]:


content.loc[2, 'Country']


# In[27]:


#content.loc[[2,5], Country]


# In[28]:


content.loc[[2,5], 'Country']


# In[29]:


content.loc[[2,5], ['Country','Item Type']]


# In[30]:


content.loc[2:7, ['Country','Item Type']]


# In[31]:


content.loc[2:7, :]


# In[32]:


content.iloc[2:7, :]


# In[33]:


content.iloc[2:7, 0:3]


# In[34]:


content = content.iloc[2:7, 0:3]


# In[35]:


content.head(8)


# In[36]:


content.describe()


# In[37]:


content.head(8)


# In[38]:




# In[43]:


plt.plot(content.Region, content.Country)


# In[44]:


plt.plot(content.Region, content.Country)


# In[45]:


plt.plot(content.Region, content.Country)
plt.xlabel('Region')
plt.ylabel('Country')
plt.show()


# In[ ]:




