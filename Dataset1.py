#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
import seaborn as sb


# **`Dataset1`**

# In[40]:


df1 = pd.read_csv('E:\python Projects\Project2\dataset_1.csv')


# **`Header`**

# In[41]:


df1.head()


# **`Number of Columns and Rows`**

# In[42]:


df1.shape


# **`dimension of Dataset1`**

# In[43]:


df1.ndim


# **`datatype of dataset1`**

# In[44]:


df1.info()


# **` season - 1 = spring, 2 = summer, 3 = fall, 4 = winter`**

# In[45]:


df1['season']= df1['season'].replace({1:'spring'})


# In[12]:


df1


# **`If day is considered a Holiday`**

# In[46]:


df1['holiday']= df1['holiday'].replace({False:'Not a Holiday'})


# In[16]:


df1


# **`working day - whether the day is neither a weekend nor a holiday`**

# In[47]:


df1[(df1['weekday']>=6)]


# In[48]:


len(df1[(df1['weekday']>=6)])


# In[53]:


df1['weekday']= df1['weekday'].replace({6:'weekday',5:'weekday',4:'weekday',3:'weekday',2:'weekday',1:'weekend Or Holiday'})


# In[60]:


df1


# **`weather:-Clear, Few clouds, Partly cloudy, Partly cloudy`**
# 

# In[59]:


df1[(df1['weathersit']==1)]


# In[57]:


df1['weathersit']= df1['weathersit'].replace({1:'Clear, Few clouds, Partly cloudy, Partly cloudy',2:'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',3:'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain         +Scattered clouds',4:'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'})


# In[58]:


df1


# In[61]:


df1['temp']


# In[62]:


df1['temp']=df1['temp'].apply(lambda x:f'feels like {int(x*100)} degree cel')


# In[63]:


df1


# **`Delete Unnecessary Columns`**

# In[64]:


df1.drop(['yr','mnth','hr'],axis=1,inplace=True)


# In[65]:


df1


# **`Missing Values of dataset1`**

# In[66]:


df1.isnull().sum()


# **`Dataset 2`**

# In[90]:


df2 = pd.read_csv('E:\python Projects\Project2\dataset_2.csv')


# **` windspeed - wind speed`**
# 
# **`Unique values of windspeed`**

# In[91]:


df2['windspeed'].unique()


# **`Mean Values of Windspeed`**

# In[92]:


df2['windspeed'].mean()


# In[93]:


df2['windspeed'].median()


# In[94]:


df2['windspeed'].mode()


# **`Mean values of non-registered user rentals`** 

# In[95]:


df2['casual'].mean()


# In[96]:


df2['casual'].median()


# In[74]:


df2['casual'].mode()


# In[97]:


df2.rename(columns={'casual':'non-registered user rentals'},inplace=True)


# In[98]:


df2


# **`registered - number of registered user rentals initiated`**

# **`unique values of registered user rentals`**

# In[101]:


df2['Registered user rentals'].unique()


# **`Missing values of dataset 2`**

# In[102]:


df2.isnull().sum()


# In[85]:


df2['atemp'].mean()


# In[45]:


df2['atemp'].fillna(df2['atemp'].mean(),inplace=True)


# In[103]:


df2.isnull().sum()


# **`Deleting Unnecessary values`**

# In[104]:


df2.drop('Unnamed: 0',axis=1,inplace=True)


# In[105]:


df2


# **`Merging dataset 1 and dataset 2`**

# In[106]:


df3 = pd.merge(df1,df2,on='instant',how='inner')


# In[107]:


df3


# **`Dataset 3`**

# In[141]:


df4 = pd.read_csv('E:\python Projects\Project2\dataset_3.csv')


# **`Header`**

# In[142]:


df4.head()


# **`tail`**

# In[143]:


df4.tail()


#  **`temp - "feels like" temperature in Celsius`**

# In[144]:


df4['temp']


# In[145]:


df4['temp']=df4['temp'].apply(lambda x:f'feels like {int(x*100)} degree cel')


# In[146]:


df4


# **`season - 1 = spring, 2 = summer, 3 = fall, 4 = winter`**

# In[147]:


df4['season']= df4['season'].replace({1:'spring'})


# In[148]:


df4


# **`holiday - whether the day is considered a holiday`**

# In[149]:


df4['holiday']= df4['holiday'].replace({False:'Not a Holiday'})


# In[150]:


df4


# In[151]:


df4[(df4['weekday']>=6)]


# In[152]:


len(df4[(df4['weekday']>=6)])


# **`working day - whether the day is neither a weekend nor a holiday`**

# In[153]:


df4['weekday']= df4['weekday'].replace({6:'weekday',5:'weekday',4:'weekday',3:'weekday',2:'weekday',1:'weekend Or Holiday'})


# In[154]:


df4


# In[155]:


df4[(df4['weathersit']==1)]


# In[156]:


df4['weathersit']= df4['weathersit'].replace({1:'Clear, Few clouds, Partly cloudy, Partly cloudy',2:'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',3:'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain         +Scattered clouds',4:'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'})


# In[157]:


df4


# In[158]:


df4.rename(columns={'casual':'non-registered user rentals'},inplace=True)


# In[159]:


df4


# In[160]:


df4['Registered user rentals'].unique()


# **`Deleting Unnecessary values`**

# In[161]:


df4.drop(['yr','mnth','hr'],axis=1,inplace=True)


# In[162]:


df4


# **`Concatenate datasets`**

# In[163]:


Final_Dataset=pd.concat([df3,df4])


# In[70]:


Final_Dataset


# In[164]:


Final_Dataset.isnull().sum()


# **`Outliers`**

# In[165]:


Q1=Final_Dataset['Total Rentals'].quantile(0.25)
Q3=Final_Dataset['Total Rentals'].quantile(0.75)
IQR=Q3-Q1
threshold=2.5


# In[182]:


outliers = Final_Dataset[(Final_Dataset['Total Rentals']<Q1-threshold*IQR) | (Final_Dataset['Total Rentals']>Q3+threshold*IQR)]


# In[183]:


outliers


# **`removing Outliers`**

# In[184]:


Final_Dataset_no_outliers = Final_Dataset.drop(outliers.index)


# In[190]:


Final_Dataset_no_outliers


# In[187]:


Final_Dataset_no_outliers.to_csv('concatenated dataset.csv')

