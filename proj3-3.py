#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

def energy(x_coord, y_coord):
    elt_spin = elt_value(x_coord, y_coord, MESH)
    neigh_sum = neighbors_sum(x_coord, y_coord, MESH)
    exter_field_sum = ext_field_sum(x_coord, y_coord, MESH)
    H = elt_spin * neigh_sum - h*exter_field_sum #total energy
    return H


# In[4]:


J = 1   #what's value of J? ask Prof
h = 1   #planck constant, he said approximate to 1??
T = 360 #Kelvin?
k = 1   #1.38 * 10**(-23)

n = 60 #dimensions NEEDS TO BE EVEN
length_grid = n
x = np.linspace(-0.5*length_grid, 0.5*length_grid, length_grid+1)  
y = np.linspace(-0.5*length_grid, 0.5*length_grid, length_grid+1)   
X, Y = np.meshgrid(x,y)

random_numbers = np.random.randint(2, size=X.shape)
MESH = random_numbers
MESH = np.where(MESH == 0, -1, MESH)

fig = plt.figure()
plt.pcolormesh(X, Y, MESH)
plt.colorbar()
#print("x = "+str(x_coord)+", y = "+str(y_coord) )


# In[ ]:


x_coord = 0
y_coord = 0

# H = energy(x_coord, y_coord)
# print("H = " + str(H))

MESH_new = MESH
for times in range(0, 1000000):
    x_coord = rd.randint(1,n)
    y_coord = rd.randint(1,n)
    E1 = energy(x_coord, y_coord)
    MESH_new[x_coord, y_coord] = -MESH_new[x_coord, y_coord]
    E2 = energy(x_coord, y_coord)
    delE = E1-E2
#         print(E1)
#         print(E2)
#         print(delE)
#         print("")
    if delE>=0: #or np.random.rand() < np.exp(-delE/(k*T)): #flip it back
        MESH_new[x_coord, y_coord] = -MESH_new[x_coord, y_coord]
            
fig = plt.figure()
plt.pcolormesh(X, Y, MESH_new)
plt.colorbar()


# In[ ]:





# In[ ]:





# In[ ]:




