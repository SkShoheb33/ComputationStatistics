#!/usr/bin/env python
# coding: utf-8

# In[63]:


import numpy as np
x = np.array(list(map(int,input().split())))
y = np.array(list(map(int,input().split())))


# In[64]:


import pandas as pd


# In[74]:


rank_x = []
rank_y = []
x_copy = np.copy(x)
y_copy = np.copy(y)
x_copy = np.sort(x_copy)[::-1]
y_copy = np.sort(y_copy)[::-1]
for i in x:
    result = (np.where(x_copy==i))
    rank_x.append((result[0][0]+1))
for i in y:
    result = (np.where(y_copy==i))
    rank_y.append((result[0][0]+1)/np.count_nonzero(x==i))
print(rank_x,rank_y)


# In[71]:


rank_x = np.array(rank_x)
rank_y = np.array(rank_y)
di = np.subtract(rank_x,rank_y)
di2 = di**2
di2_sum = sum(di2)
n = len(x)
row  = 1-(6*di2_sum)/(n*(n**2-1))
print(row)

