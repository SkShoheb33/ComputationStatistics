#!/usr/bin/env python
# coding: utf-8

# In[39]:


import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np


# In[65]:


dataFrame = pd.read_csv("Z:\\Computer Statistics\\temperatures.csv")
plt.figure(figsize=(15,12))
plt.plot(dataFrame.YEAR,dataFrame.ANNUAL,marker="+",color="red")
plt.xlabel("YEAR")
plt.ylabel("ANNUAL")
plt.title("YEAR/ANNUAL")
plt.show()


# In[61]:


reg = linear_model.LinearRegression()
reg.fit(dataFrame[['YEAR']],dataFrame.ANNUAL)


# In[64]:


y_predict = []
x = []
for i in dataFrame.YEAR:
    x.append(i)
    y_predict.append(reg.predict([[i]]))
plt.figure(figsize=(15,12))
plt.scatter(dataFrame.YEAR,dataFrame.ANNUAL,marker="+",color="red")
plt.plot(x,y_predict,color="green")
plt.xlabel("YEAR")
plt.ylabel("TEMPERATURE")
plt.title("YEAR v/s TEMPARATURE")
plt.show()


# In[63]:


x = np.array(dataFrame.YEAR)
y = np.array(dataFrame.ANNUAL)
n = len(x)
sigma_x = sum(x)
sigma_y = sum(y)
sigma_xy = sum(np.multiply(x,y))
sigma_x2 = sum(x**2)
m = (n*sigma_xy-sigma_x*sigma_y)/(n*sigma_x2-sigma_x**2)
c = (sigma_y-m*sigma_x)/n
print(m,c)
print(reg.coef_,reg.intercept_)

