#!/usr/bin/env python
# coding: utf-8

# #### Import Necessary Libraries

# In[68]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import math


# In[127]:


all_data=pd.read_csv('./Sample Data/FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin_1')


# #### Answer the following questions based on the African food production dataset provided by the FAO website already provided
# 
# #### Question 11
# What is the total sum of Animal Fat produced in 2014 and 2017 respectively?
# 
# Hint:
# 
# Perform a groupby sum aggregation on ‘Item’

# In[155]:


all_data.groupby('Item')[['Y2014', 'Y2017']].sum().filter(like='Animal fats', axis=0)


# #### Question 12
# What is the mean and standard deviation across the whole dataset for the year 2015 to 3 decimal places?

# In[169]:


np.round((all_data['Y2015'].mean(), all_data['Y2015'].std()),3)


# #### Question 13
# What is the total number and percentage of missing data in 2016 to 2 decimal places?

# In[168]:


(all_data['Y2016'].isnull().sum(), np.round(((all_data['Y2016'].isnull().sum() / all_data['Y2016'].count())*100),2))


# In[103]:


(all_data['Y2016'].isnull().sum() / all_data['Y2016'].count())*100


# #### Question 14
# Which year had the highest correlation with ‘Element Code’? 

# In[181]:


all_data.corr().filter(like='Element Code', axis=0)


# #### Question 15
# What year has the highest sum of Import Quantity?
# 
# Hint- Perform a groupby operation on ‘Element’ and use the resulting Dataframe to answer the question

# In[186]:


all_data.groupby('Element').sum().filter(like='Import Quantity', axis=0)


# #### Question 16
# What is the total number of the sum of Production in 2014?
# 
# Hint- Perform a groupby operation on ‘Element’ and use the resulting Dataframe to answer the question

# In[188]:


all_data.groupby('Element')['Y2014'].sum().filter(like='Production', axis=0)


# #### Question 17
# Which of these elements had the highest sum in 2018?
# 
# Hint-  Select columns ‘Y2018’ and ‘Element’, Perform a groupby operation on ‘Element’ on the selected dataframe and answer the  question.

# In[190]:


all_data.groupby('Element')['Y2018'].count()


# #### Question 18
# Which of these elements had the 3rd lowest sum in 2018?
# 
# Hint-  Select columns ‘Y2018’ and ‘Element’, Perform a groupby operation on ‘Element’ on the selected dataframe and answer the  question.

# In[193]:


all_data.groupby('Element')['Y2018'].count()


# #### Question 19
# What is the total Import Quantity in Algeria in 2018?

# In[152]:


all_data.loc[all_data['Area']=='Algeria']


# #### Question 20
# What is the total number of unique countries in the dataset?

# In[192]:


all_data.groupby('Area')['Y2018'].sum().count()


# In[ ]:




