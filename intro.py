# pip install numpy

import numpy as np

# array initializes as :

# one dimensional array
# ======================
# array contains  a single rows of elements are termed as one dimensional array

# elements = np.array([1,2,3,4])

# print(elements) # [1 2 3 4]

# print(elements.ndim) # 1 (one dimensional)
# print(elements.shape)  

# Two dimensional array
# ========================

# array with elements in multiple rows (table like format)
# np.array([row1],row[2]) can be termed as two dimensional array

# elements_2 = np.array([[1,2,3,4],[5,6,7,8]])

# print(elements_2)
# print(elements_2.ndim)
# print(elements_2.shape) # 2 rows and 4 columns

# # 3 dimensional array 
# # ======================
# # 
# element_3 = np.array([
#     [[1,2,3,4],[5,6,7,8]],
#     [[1,2,3,4],[5,6,7,8]],
#     [[1,2,3,4],[5,6,7,8]]
# ])
# print(element_3)
# print(element_3.ndim)
# print(element_3.shape) 

# Atributes
# ================
# print(element_3.ndim)
# print(element_3.dtype) # int64 # returns the datatype
# print(element_3.shape) # (2,2,3)  (no of 2-dim array,no_rows in each array,no_columns)


# Types of matrices
#==================
# zero matrix
# zero matrix having 3 rows and 4 columns with integer datatpe

# m_1 = np.zeros((3,4),dtype=int)
# print(m_1)

# ones matrix
# ===================
# matrix having all elements as 1

# m_2 = np.ones((4,3),dtype=int)
# print(m_2)

# full matrix
# ==============
# (shape,value,datatype)

# m_3 = np.full((3,4),5,dtype=int)
# print(m_3)

# identity matrix
# =====================
# rows and columns should be equal
# can be used in two methods (np.identity,np.eye)

# m_4 = np.identity(n=3,dtype=int)
# print(m_4)

# print(np.eye(N=4,dtype=int))


# addition ,subtraction
# a = np.array([1,2,3,4,5,6,7,8,9,10])

# a = np.array(([i for  i in range(1,11)]))
# print(a)
# print(a.reshape(2,5))
# # used for converting one dimension array into 2-d array

# b = np.arange(9)
# print(b)

# b= np.arange(1,9).reshape(2,4).ndim
# print(b)

# b = np.array([[1,2,3,4],[5,6,7,8]])
# print(b.flatten()) # converting 2-d / 3-d into 1 dimensional array

# a = np.array(([3,2,4,1],[6,4,2,1]))
# b = np.array(([1,2,3,4],[5,6,7,8]))

# print(a)

# print(b)

# print(np.add(a,b))

# print(a + b)
# print(np.subtract(a,b))
# print(np.multiply(a,b))
# print(np.divide(a,b))

# print(np.square(a))

# print(np.sqrt(a))



# a = np.array([[3,2,4,1],[6,4,3,1]])
# print(a ** 2) # vector calculation
# print(a*2)
# print(a /2)

# print(np.sum(a,axis = None)) # 24
# print(np.sum(a,axis=1))
# print(np.sum(a,axis=0))

# sorting in array
# ===================
# arrange the elements in ascending or descending order

# rev = np.sort(a,axis = 1)[:,::-1]
# print(rev)

# np.sort() returns the array in ascending order
# np.sort(a,axis = 1)[:,::-1] # in descending order
# we are using slicing technique so need to give row index and column index

# arr = np.arange(1,21).reshape(5,4)
# print(arr)

# col index
"""
[[ 1  2  3  4] 
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]] # row index

 """

# arr[row start:row stop,column start:column stop]

# print(arr[1:3,1:3])

# print(arr[2:4,1::])  # 1:: ( upto last)
# #[[10 11 12]
# #  [14 15 16]]


# print(arr[1:4,2::])

# print(arr[1:4,0:2])

arr_2 = np.array([4,3,5,7,2,10])

print(arr_2.argmax()) # returns the index of the largest element

print(arr_2.argmin()) # returns the index of the smallest element

print(arr_2.argsort())


# arr_3 = np.array([[1,2,3,4],[4,5,6,7],[8,10,12,14]])
# print(arr_3.argmax())  # 11 return the index after flatten the 2d array.

arr_3 = np.array([[1,2,3,4],[4,5,6,7],[8,10,12,14]])
print(np.where(arr_3 > 5))
#      row index                        column index
#(array([1, 1, 2, 2, 2, 2]), array([2, 3, 0, 1, 2, 3]))

print(np.where(arr_3 > 5 , "pass","fail"))
# np.where(condition.value_if_true,value_if_false) # replacing condition
# [['fail' 'fail' 'fail' 'fail']
 #['fail' 'fail' 'pass' 'pass']
 #['pass' 'pass' 'pass' 'pass']]



# print(arr_3.argmax(axis = 0))
# print(arr_3.argmax(axis = 1))

# print(arr_3.argmin(axis = 1))
# print(arr_3.argmin(axis = 0))


# print(arr_2)

# np.where(condition)
# use to positioning the elements which satisfy the condition
# print(np.where(arr_2 > 5)) # (array([3, 5]),)






































