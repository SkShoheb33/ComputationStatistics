#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
x = np.array(list(map(int,input("Enter x : ").split())))
y = np.array(list(map(int,input("Enter y : ").split())))


# In[20]:


xy = x*y
x2 = x**2
y2 = y**2
x_bar=np.mean(x)
y_bar=np.mean(y)
print(x_bar,y_bar)


# In[21]:


cov = np.mean(xy)-(x_bar*y_bar)
cov


# In[22]:


import math as mt
sigma_x = mt.sqrt(np.mean(x2)-x_bar**2)
sigma_y = mt.sqrt(np.mean(y2)-y_bar**2)
print(sigma_x,sigma_y)


# In[23]:


r  = cov/(sigma_x*sigma_y)
r

