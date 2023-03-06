#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing pandas and numpy 
import pandas as pd
import numpy as np


# # 1) Downloading the auto data set

# In[4]:


#downloading the auto data set
df= pd.read_csv('autos.csv')
df


# # 2) Print out first 8 rows

# In[5]:


df.head(8)


# # 3)Return a data frame containing the minimum price of cars

# In[7]:


#Returning the dataframe of minimum prices of each car
gpd_a= df.groupby('make')
min_price = gpd_a['price'].min()
min_price


# # 4) What is the smallest standard deviation of the prices 

# In[9]:


std_dev =np.std(df).min()
std_dev


# 
# # Return the last 2 rows of each group of car make and fuel_type

# In[10]:


col = ['make','fuel_type']
print(df[col].tail(2))


# # 6) Replicate the split-apply-combine without GroupBY 

# In[12]:


dict_1 ={'make':['Alfa','benz','audi','saab'],'price':[25580,56444,36215,12548]}
dict_2 ={'make':['volvo','Toyota','vitz','nissan'],'Price':[38792,478915,897452,59864]}
df_1 = pd.DataFrame(dict_1)
df_2 = pd.DataFrame(dict_2)
merge_df = pd.concat([df_1, df_2],ignore_index=True)
merge_df


# In[ ]:




