#!/usr/bin/env python
# coding: utf-8

# # Advanced Python for Cognitive Scientists
# ### Marcin Lesniak, Ph.D.
# Warszawa 2021/22

# ## Assignment 2.
# 
# The file `tms_phosphenes.csv` contains results of TMS mapping of one participant's occipital cortex. To perform the mapping a grid of targets was used, similar to this one:
# 
# <img src="https://drive.google.com/uc?export=view&id=1ss2bnYNyahMhgteZx0-x4JSv9RbFsnuB" style="height: 200px; width: auto">
# 
# 
# The mapping procedure was repeated 10 times. Thus, each of 10 grids (15 x 21) contain individual responses to a single TMS pulse. `1` means that the participant reported phosphenes directly after the TMS pulse application; `0` means failure of phosphene elicitation from that particular site.
# 
# Your task is to: 
# 1. Merge all grids so that they represent probability of phosphene elicitation in all sites - use NumPy array.
# 2. Using as a threshold 60% probability, replace all subthreshold probabilities with `0`.
# 3. Add **x** and **y** coordinates, so that the central point of the grid was represented as `x = 0` and `y = 0`:
#     * Add x axis (ranging from -10 to 10) on the top of the array
#     * Add y axis (ranging from -7 to 7) on the left side of the array
#     
#     The final array should like like this:
#     
#     ```
#      [[  0 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10]
#        [ -7   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
#        [ -6   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
#        [ -5   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
#        [ -4   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
#        [ -3   0   0   0   0   0   0   0  70   0  60   0   0   0   0   0   0   0   0   0   0   0]
#        [ -2   0   0   0   0   0   0  80   0  80 100  70  60  70  60   0   0  70   0   0   0   0]
#        [ -1   0   0   0   0   0  60  80 100  80  60  80 100  80  80  80  80   0   0   0   0   0]
#        [  0   0   0   0   0  60  70  60  80  80  80  90  80  70  80  70  60   0   0   0   0   0]
#        [  1   0   0   0   0   0  80  60   0  80  80  80  90  70  80   0  90   0   0   0   0   0]
#        [  2   0   0   0   0   0   0   0  90  70  70  60  60  80   0   0   0   0   0   0   0   0]
#        [  3   0   0   0   0   0   0   0   0   0   0  60   0   0   0   0   0   0   0   0   0   0]
#        [  4   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
#        [  5   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
#        [  6   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
#        [  7   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]]
#     ```
#     
# 4. Display coordinates of all sites/targets where probabilities were maximal, e.g. like this:
# 
#     ```
#     Nr 1.
#     x: -1, y: -2
# 
#     Nr 2.
#     x: -3, y: -1
# 
#     Nr 3.
#     x: 1, y: -1
#     ```
# 
# HINTS:
# * In order to read the file directly to a NumPy array you may use: 
# ```python
# my_array = np.genfromtxt(path_to_file, delimiter=';', dtype = int)
# ```
# * Review the CSV file and see how the data is arranged, before you start writing the code.
# * Array vectorization (scalar and array-array), aggregation methods, as well as boolean indexing will be very helpful. 

# In[1]:


import numpy as np

# this will ensure proper alignment of arrays in the output of jupyter notebook (without wrapping)
np.set_printoptions(linewidth = 120)


# In[2]:


# The path needs to be changed accordingly; does genfromtxt accept url links as a file path though?
path='C:/Users/julia.DESKTOP-0ILPF3P/OneDrive/Desktop/STUDIAAA/kognitywistyka/K2/K2.1/sem1/advanced python/assignment 2/tms_phosphenes.csv'

my_array = np.genfromtxt(path, delimiter=';', dtype = int) # huge array of all responses
A = np.delete(my_array, np.where(my_array[:,0]==-1)[0], 0) # deleting the rows filled with -1 (rows filled with ;;;;; in the csv file)

# Generating grids from the initial array
# Kind of a tedious method, totally not what I wanted to do, but I had an art block and couldn't come up with a better idea
grid1=A[:15,:]
grid2=A[15:30,:]
grid3=A[30:45,:]
grid4=A[45:60,:]
grid5=A[60:75,:]
grid6=A[75:90,:]
grid7=A[90:105,:]
grid8=A[105:120,:]
grid9=A[120:135,:]
grid10=A[135:150,:]


# In[3]:


# TASK 1: merging all grids and multiplying values by 10 to represent percentages
merged_grid=(grid1+grid2+grid3+grid4+grid5+grid6+grid7+grid8+grid9+grid10)*10
merged_grid


# In[4]:


# TASK 2: replacing all subthreshold values with 0
merged_grid[merged_grid<60]=0
merged_grid


# In[5]:


# TASK 3: adding x and y axes to the grid

x_axis=np.arange(-10,11)

y_axis=np.array([0]) # started creating y axis by 0, appending it by an array ranging from -7 to 7
y_axis=np.hstack((y_axis,np.arange(-7,8)))

X=np.vstack((x_axis,merged_grid)) # adding x axis to the merged grid, creating a temporary grid X
final=np.hstack((y_axis.reshape(16,1),X)) # adding y axis to the temporary grid X, creating the final grid

final


# In[6]:


# TASK 4: displaying the coordinates of all sites where probabilities were maximal

ind=np.asarray(np.where(final==100)).T # getting indices of all 'maximal' sites in an easy-to-read array

print('Probabilities were maximal at:\nNr 1.: x =',final[0,ind[0,1]],'y =',final[ind[0,0],0],'\nNr 2.: x =',final[0,ind[1,1]],'y =',final[ind[1,0],0],'\nNr 3.: x =',final[0,ind[2,1]],'y =',final[ind[2,0],0])

