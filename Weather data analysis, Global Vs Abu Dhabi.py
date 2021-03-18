#!/usr/bin/env python
# coding: utf-8

# # Importing libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


# # Reading csv and creating dataframe

# In[2]:


df = pd.read_csv( r'C:\Users\Deepak\abudhabi_avg_temp.csv', )


# In[3]:


df


# In[10]:


df.describe


# # Smooth out the data , 
# by calculating moving average of Global and Abu Dhabi avg temp, Rolling avg is related to rolling at 10

# In[9]:


gavg = df['gavg'].rolling(10).mean()
gavg


# In[7]:


cavg = df['cavg'].rolling(10).mean()
cavg


# # Plotting data

# In[16]:


#matplotlib used for plotting
#this plot shows yearly global trend of average temperature
plt.plot(df['year'],gavg,label='Global')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Global Yly Avg Temp Trend")
plt.show()


# In[17]:


#this plot shows yearly Abu Dhabi trend of average temperature
plt.plot(df['year'],cavg,label='Abu Dhabi')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Abu Dhabi Yly Avg Temp Trend")
plt.show()


# In[19]:


plt.plot(df['year'],gavg,label='Global')
plt.plot(df['year'],cavg,label='Abu Dhabi')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Temperature (°C)") 
plt.title("Global Vs Abu Dhabi Yly Avg Temp Trend")
plt.show()


# In[ ]:


#seaborn is not used for line plotting

