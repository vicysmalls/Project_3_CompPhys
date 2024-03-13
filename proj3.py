#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random as rd
import numpy as np
import matplotlib.pyplot as plt

def elt_value(x_coord, y_coord, MESH): #get value at (x,y)
    self_mask = ((X-x_coord)==0) * ((Y-y_coord)==0)
    if np.sum(self_mask*MESH) == 1:
        return 1
    else:
        return -1
        
def neighbors_sum(x_coord, y_coord, MESH): #get sum of values around (x,y) (no diagonal)
    neighbors_mask = ( (((X-x_coord)==0) * (np.abs(Y-y_coord)<2) 
            +(np.abs(X-x_coord)<2) * (np.abs(Y-y_coord)==0))
            *(1-(((X-x_coord)==0) * ((Y-y_coord)==0))) )
    return np.sum(MESH*neighbors_mask)

def ext_field_sum(x_coord, y_coord, MESH): #gets values of external field (see slack file)   
    ext_field_mask = ((Y-y_coord)==0) *(1-(((X-x_coord)==0) * ((Y-y_coord)==0))) 
    return np.sum(MESH*ext_field_mask)


# In[24]:


n = 160 #dimensions NEEDS TO BE EVEN
length_grid = n
x = np.linspace(-0.5*length_grid, 0.5*length_grid, length_grid+1)  
y = np.linspace(-0.5*length_grid, 0.5*length_grid, length_grid+1)   
X, Y = np.meshgrid(x,y)

random_numbers = np.random.randint(2, size=X.shape)
MESH = random_numbers
MESH = np.where(MESH == 0, -1, MESH)


# In[25]:


x_coord = 3
y_coord = 3
print("x = "+str(x_coord)+", y = "+str(y_coord) )
fig = plt.figure()
plt.pcolormesh(X, Y, MESH)
plt.colorbar()
   
elt_spin = elt_value(x_coord, y_coord, MESH)
neigh_sum = neighbors_sum(x_coord, y_coord, MESH)
exter_field_sum = ext_field_sum(x_coord, y_coord, MESH)    
    
J = 1  #what's value of J? ask Prof
h = 1  #planck constant, he said approximate to 1??
H = elt_spin * neigh_sum - h*exter_field_sum #total energy

print("H = " + str(H))


# In[ ]:




