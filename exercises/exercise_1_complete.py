# Exercise 1
# 10/02/2025

# Read a list from the file "ex_1_data_in.dat" file. 
# Take the square root of each element of the list and 
# save the resulting lists in the file ex_1_data_out.dat
# Such file must have two columns: the first one should
# contain the original list; the second one the computed
# square root.

import numpy as np

file_in="ex_1_data_in.dat" 
file_out="ex_1_data_out.dat"

# Load the datafile in the numpy array
# data_in
data_in=np.loadtxt(file_in)

# Store in the variable num_data the number of elements in 
# the array data_in
num_data=len(data_in)

# Compute the square root of the elements in data_in
# and save the results in the array data_out
data_out=np.sqrt(data_in)

# Create the 1D-array data_total by appending
# data_out to data_in 
data_total=np.append(data_in, data_out)

# Reshape the 1D array data_total in a 2D array
# of 2 columns and num_data rows.
# For example, imagine you have two 1D arrays a and b, such that
#    a=[1,2,3]
#    b=[4,5,6]
# Then ab=np.append(a,b) produces
#    ab=[1,2,3,4,5,6]
# and ab=reshape(ab, (2, 3)) produces
#    ab=[[1,2,3]
#       [4,5,6]] 

data_total=np.reshape(data_total, (2, num_data))

# Now, take the transpose of data_total: you get
# a 2D array of num_data rows and 2 columns.
# In the example above, 
#    ab=[[1,4]
#        [2,5]
#        [3,6]]

data_total=np.transpose(data_total)

# Save the array in the file file_out
np.savetxt(file_out, data_total, fmt='%.2f %.4f')
