import numpy as np

#!-------------Creation of Arrays--------------------!#
# creates an empty array
# creates an array with start value as 1
# end value as 10 and step value as 2.
print("\n---------------------------------------------------------------------------------------\n")
aray=np.array([]) 
aray=np.arange(1,10,2)
print(aray)
print("\n---------------------------------------------------------------------------------------\n")
#creates an array with five entries between 1 and 20
#where each value has equal space between them.
aray = np.linspace(1,20,5)
print(aray)
print("\n---------------------------------------------------------------------------------------\n")
#creates an array with default value of 1
#the dimensions has to be specified and
#the datatypes of the array could be optionally provided

aray = np.ones((2,2),dtype='int')
print(aray)
print("\n---------------------------------------------------------------------------------------\n")
#creates a 2 x 8 array with zero as the default value.
aray = np.zeros((2,8))
print(aray)
print("\n---------------------------------------------------------------------------------------\n")
#creates an 2 x 10 uninitialized array
#the value of the arrays are arbitrary
#as available in the memory

aray = np.empty((2,2))
print(aray)
print("\n---------------------------------------------------------------------------------------\n")
#creates a 3 x 2 array with random values between 0 and 1.
aray = np.random.rand(3,2)
print(aray)
print("\n---------------------------------------------------------------------------------------\n")
#create an array with ten elements
aray = np.arange(0,10,1)
print(aray)
print("\n---------------------------------------------------------------------------------------\n")

#!---------------------Array Manipulation-------------------------------------
#-----------------------------------------------------------

print("\n---------------------------------------------------------------------------------------\n")
#Returns an reshaped array(5x2) for the 1-D array 'aray'
r_aray= np.reshape(aray,(5,2))
print(r_aray)
#An another variation of reshape with the second parameter -1, which indicates
#that the dimension should be automatically calculated based on the size of
#the array and the other specified dimension.
print(r_aray.shape)
print(r_aray.reshape(-1,1))

print("\n---------------------------------------------------------------------------------------\n")
#shape is used to get the dimension of the array
print(r_aray.shape)
print("\n---------------------------------------------------------------------------------------\n")
#Returns an 1D array 
anaray =r_aray.flatten()
print(anaray)
print("\n---------------------------------------------------------------------------------------\n")
#returns a transposed array/matrix
print(r_aray)
aray = r_aray.transpose()
print(aray)

print("\n---------------------------------------------------------------------------------------\n")
#This function returns a concatenated array and
#the concatenation could be either rowwise or
#column wise depending upon the second paramenter 'axis'
#axis can take value 0 or 1.
#0 indicates row wise conctenation,1 means column wise concatenation.
aray1 = np.arange(1,10,1).reshape(3,3)
aray2 = np.arange(11,20,1).reshape(3,3)
aray3 = np.arange(21,30,1).reshape(3,3)
print(aray1)
print(aray2)
print(aray3)

concat_aray = np.concatenate((aray1,aray2,aray3),axis=1)
print(concat_aray)

print("\n---------------------------------------------------------------------------------------\n")
#We will now use the concat_aray and split it into 3 halves
#by using the np.split method. Again,whether the split should
#be based on row or column is decided by the axis parameter.
split_aray = np.split(concat_aray,3,axis=1)
print(split_aray)

#!---------------------Array Manipulation-------------------------------------
#-----------------------------------------------------------
#Mathematical Operations
print("\n---------------------------------------------------------------------------------------\n")
aray = np.array([[1,2],[3,4]])

#Calculates the sum of elements in the array

aray_sum = np.sum(aray)
print(aray_sum)

print("\n---------------------------------------------------------------------------------------\n")

#Determines and returns the mean of element in the aray
aray_mean = np.mean(aray)
print("Means is :",aray_mean)

print("\n---------------------------------------------------------------------------------------\n")

#Returns the maximum element in the aray
maxin_aray = np.max(aray)
print("The maximum element in an array is {0}".format(maxin_aray))

#Returns the minimum element in the arary.
minin_aray = np.min(aray)
print("The minimum element in the array is {0}".format(minin_aray))
print("\n---------------------------------------------------------------------------------------\n")

#Returns the standard deviation of the elements in the array
aray =np.array([[3,4,5,2,3,4]]).reshape(2,3)
sdeviation = np.std(aray)
print(sdeviation)





