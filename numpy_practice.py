#Created by Yash Bhardwaj 

#NUMPY TUTORIAL


#Comment out the piece of code you dont want to run and check in the compiler as you read it.
#PS - I know I should have written it in Jupyter Notebook (my bad) but by the time I realized this, I had already written 500 lines of code.



import numpy as np 


#printing an array
a = np.array([1,2,3])
print(a)


dt = np.dtype(np.int32)
print(dt)

dt = np.dtype('i4')
#int8, int16, int32, int64 are read in tables of 8: 'i1'.'i2','i4','i8'
print(dt)
dt = np.dtype('i8')
print(dt)

#complex implementation
a = np.array(a,dtype = complex)
print(a)


dt = np.dtype([('age',np.int8)])
print(dt)
a = np.array([10,20,30],dtype = dt)
print(a['age'])

#Applying a structured dtype object to an ndarray 
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
a = np.array([('abc',21,55.4),('hellofren',57,33),('lastone',19,88)],dtype = student)
print(a)


#ARRAY ATTRIBUTES:

#Reshaping/Resizing the array
a = np.array([[1,2,3],[4,5,6]])
print(a)
print("\nThe shape is: ")
print(a.shape)
a.shape = (3,2)
print("\n New shape is: ")
print(a)

print(a.reshape(2,3))
print(a.reshape(1,6))
print('\n')

#Using np.arange() and calculating number of dimensions
#Changing the dimensions of an ndarray
nums = np.arange(24)
print(nums)
print(a.ndim)
print('\n')
print(nums.reshape(2,4,3))
print(nums)
print('\n')

#Using ndarray.itemsize and ndarray.flags
x = np.array([1,2,3,4,5],dtype = np.float)
print(x.itemsize)
print(x.flags)
print('\n')



#NUMPY ARRAY CREATION ROUTINES:

#np.empty
x = np.empty([3,3],dtype = int, order = 'C')
print(x)
print('\n')

#np.zeros
x = np.zeros((2,2),dtype = np.int)
print(x)
print('\n')
x = np.zeros((2,2),dtype = [('x','i4'),('y','i4')])
print(x,x.ndim)

#np.ones
x = np.ones(5,dtype = int)
print(x)
print('\n')
x = np.ones([2,3],dtype = np.int)
print(x)

#ARRAY FROM EXISTING DATA

#np.asarray
#Creating numpy array from a normal python array:
x = [1,4,66,56]
print(x)
print('\n')
a = np.asarray(x)
x = np.reshape(x,(2,2)) 
print(x, x.ndim)
print('\n')
b = np.asarray(x,dtype = float)
print(b)
print('\n')

#ndarray or a numpy array can also be created from a tuple/list of tuples/tuples of lists:
x = (1,2,3,4,5,5)
a = np.asarray(x,dtype = int)
print(a)
print('\n')

#np.frombuffer function allows splitting chars of a string and storing each char as a numpy element:
#<The follwing block needs to be debugged>
#s = 'Hello World' 
#a = np.frombuffer(s, dtype = 'S1')
#print(a)
print('\n')

#np.fromiter - builds an ndarrray/numpy array from any iterative object.A new array is returned.
list1 = range(5)
print(list1)	#will show variable list1 as a 'range' object
it = iter(list1)	#converts 'range' into range iterator object
print(it)	
x = np.fromiter(it, dtype = int)	#converts range iterator into numpy array object
print(x)

#NUMPY ARRAY FROM NUMERICAL RANGES

#numpy.arange(start,stop,step,dtype)
x = np.arange(5)
print(x)
print('\n')
#setting dtype
x = np.arange(6,dtype = float)
print(x)
print('\n')
#using start and stop parameters: 
x = np.arange(10,20,2,dtype = int)
print(x)
print('\n')

#numpy.linspace(start,stop,num,endpoint,retstep,dtype)
#This function is similar to np.arange(), instead of step, it takes number of divisions as input parameter
x = np.linspace(10,20,5,dtype = float)
print(x)
print('\n')
x = np.linspace(10,20,6,dtype = int)
print(x)
#Note - By default, endpoint = True, hence last value is included.
print('\n')
#if retstep = True, it returns the step between the numbers.
x = np.linspace(10,20,6,dtype = int,retstep = True)
print(x)
print('\n')

#numpy.logspace(start,stop,num,endpoint,base,dtype)
#start and stop endpoints of the scale are indices of the base, usually 10.

#start - starting point of the sequence is base^start.
#stop - final value of sequence is base^stop
#num - number of values between the range. Default is 50.
#endpoint - If True(default), stop is last value in range
#base - Base of logspace (10 by default)
#dtype - data type of output array. If not given, it depends upon other input arguments.

a = np.logspace(1.0,2.0,num = 10)
print(a)
print('\n')
#set base = 2
a = np.logspace(1,10,num = 10,base = 2)
print(a)
print('\n')
print('\n')


#INDEXING AND SLICING: 

#3 types of slicing methods are available - field access, basic slicing, advanced indexing
#basic slicing is  an extension of Python's concept of slicing to n dimensions.
#A Python slice object is made by giving 'start','stop','end' parameters to the built-in slice function
#The slice object is passed to the array to extract the part of the array.

a = np.arange(10)	#prepares an ndarray object
s = slice(2,7,2)	#slice object with start,stop and step parameters
print(a[s])			#slice object passed to the array
print('\n')
print(a[2:7:2])	#Note this can also be directly passed to the array separated by ":"
print('\n')
print(a[2:7])
print('\n')

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print('\n')
print('Array sliced from index 1:')
print(a[1:])
print('\n')
print('\n')

#Slicing can also include ellipsis (...) to make a selection tuple same as the dimension of the array
#If ellipses is used at row position, it returns an ndarray comprising of items in rows.

print("Our array is: ")
print(a)
print('\n')

#This returns the tiems in second column:
print('Items in second column are: ')
print(a[...,1])
print('\n')

#this array returns the items in second row:
print('Items in second row are: ')
print(a[1,...])
print('\n')

#Slicing all items from column 1 onwards
print('The items from column 1 onwards are: ')
print(a[...,1:])
print('\n')
print('\n')

#ADVANCED INDEXING

#It is possible to make a selection from ndarray that is a non-tuple sequence, 
#ndarray object of intger of Boolean data type, or a tuple with at least one item being a
#sequence object. Advanced indexing returns a copy of the data. Slicing only presents a view

#There are two types of advanced indexing - Integer and Boolean

#Integer Indexing:

#Each integer array represents the number of indexes into that dimension.
#When the index consists of as many integer arrays as the dimensions of the target ndarray, 
#it becomes straightforward.

#In the following example,
#one element of specified column from each row of ndarray object is selected.
#Hence, the row index contains all row numbers, and the column index specifies the element to be selected.

x = np.array([[1,2],[3,4],[5,6]])
print("Array x is: \n")
print(x)
print('\n')
y = x[[0,1,2],[0,1,0]]
print("integer slicing at x coordinates(0,1,2) and y coordinates(0,1,0): \n")
print(y)
print('\n')

#Now this shit is gonna get a bit more complicated:
x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])

print('Our array is: \n')
print(x)
print('\n')

#This shit right here is very important:
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])

y = x[rows,cols]
print('The corner elements are: ')
print(y)
print('\n')
print('\n')

#Advanced and basic indexing can be combined by using one slice (:) or ellipsis (…) with an index array. 
#The following example uses slice for row and advanced index for column. 
#The result is the same when slice is used for both. 
#But advanced index results in copy and may have different memory layout.

x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print('Our array is: \n')
print(x)
print('\n')

#slicing: 
z = x[1:4,1:3]	#rows index 1 through 4(not included), column index 1 through 3(not included)

print("After slicing as z = x[1:4,1:3], our array is: \n")
print(z)
print('\n')

#using advanced index for column:
y = x[1:4,[1,2]]
print('Slicing using advanced index for column: \n')
print(y)
print('\n')
print('\n')
#somebody please explain this last implementaion of advanced slicing right above!!!


#BOOLEAN ARRAY INDEXING

#This type of advanced indexing is used when the resultant object is meant to be the result of Boolean operations,
#such as comparison operators.

x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print('Our array is: \n')
print(x)
print('\n')

#we will print items greater than 5:
print('The items greater than 5 are: ')
print(x[x>5])
print('\n')

#**Filtering out complex elements from an array:**
a = np.array([1,5,3+6j,9+1j])
print('Our array is: ')
print(a)
print('\n')
print('The complex elements are: ')
print(a[np.iscomplex(a)])
print('\n')
print('\n')


#BROADCASTING


#Broadcasting refers to the ability of Numpy to treat arrays of different shapes during operations
#Arithmetic operations on arrays are usually done on corresponding elements. 
#If two arrays are exactly of the same shape, then operations are smoothly performed. 

#Check out this simple example:

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a*b
print(c)
print('\n')
#See? Smooth right? That is because they are both 1x4 arrays.

#For two dissimilar arrays, element to element arrays are not possible.
#But broadcasting allows such operations to be easily performed.
#The smaller array is BROADCAST to the larger array.

#RULES for BROADCASTING:

#1. Broadcasting is possible when array with smaller ndim than the other is prepared with '1' in its shape
#2. Size in each dimension of the output shape is maximum of the input sizes in that dimension
#3. An input can be used in calculation, if its size in a particular dimension matches the output size or its value is exactly 1
#4. if an input has a dimension of 1, the first data entry in that dimension is used for all calculations along that dimension.


#A set of arrays is said to be broadcastable if the above rules produce a valid result and one of the following is true −

#1. Arrays have exactly the same shape.
#2. Arrays have the same number of dimensions and the llength of each dimension is either a common length or 1.
#3. Array having too few dims can have its shape prepended with a dim of lenght 1, so that the above property is True


#Check out an example of Broadcasting: 

a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])  

print('First array: ')
print(a)
print('\n')
print('Second array: ')
print(b)
print('\n')
print('Sum: ')
print(a+b)
# or for ints, print(np.array(a+b,dtype = int))
print('\n')
print('\n')



#ITERATING OVER ARRAY:


#Numpy conntains an iterator object called *numpy.nditer* 
#It is an efficient multidimesionl iterator object using which it is possible to iterate over an array.
#Each element of an array is visited using Python's standard iterator interface. 



a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is: ')
print(a)
print('\n')

print('Modified array is: ')
for x in np.nditer(a):
	print(x)
print('\n')	 
print('\n')






#The order of iteration is chosen to match the memory layout of an array, without consideringa particular ordering.
#This can be seen by iterating over the transpose of the above array.

a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is: ')
print(a)
print('\n')

print('Transpose of array is: ')
b = a.T
print(b)
print('\n')
print('Modified array is: ')
for x in np.nditer(b):
	print(x)

print('\n')	


#ITERATION ORDER - If the same elements are stored using F-style order, 
#the iterator chooses more efficient way of iterating over an array.


#C-Style Order - Iterates over a row, across all rows.
#F-Style Order - Iterates over a column, across all columns.


a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is: ')
print(a)
print('\n')

print('Transpose of array is: ')
b = a.T
print(b)
print('\n')

print('Sorted in C-Style order: ')
c = b.copy(order = 'C')
print(c)
print('\n')
for x in np.nditer(c):
	print(x)


print('\n')

print('Sorted in F-Style order: ')
c = b.copy(order = 'F')
print(c)
print('\n')
for x in np.nditer(c):
	print(x)

print('\n')	
print('\n')

#NOTE - It is aslo possible to force 
#the nditer object to use a specific order by explicitly mentioning it.
#The following is a more efficient implementation of the above:


a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print('Original array is:') 
print(a) 
print('\n')  

print('Sorted in C-style order:') 
for x in np.nditer(a, order = 'C'): 
	print(x)  

print('\n') 

print('Sorted in F-style order:') 
for x in np.nditer(a, order = 'F'): 
   print(x)

print('\n')
print('\n')


#MODIFYING ARRAY VALUES***

#The nditer object has another parameter called op_flags.
#Its default value is read only, but can be set to read-write or write-only mode.
#This will enable modifying array elements using the iterator while iterating.

a = np.arange(0,60,5)
a = a.reshape(3,4)

print('The original array is: ')
print(a)
print('\n')

for x in np.nditer(a,op_flags = ['readwrite']):
	x[...] = 2*x							#Note [...] is necessary. rememeber that.

print('The modified array is: ')
print(a)
print('\n')
print('\n')


#EXTERNAL LOOP - 

#The nditer class constructor has a 'flags' parameter, which can take the following values - 

#c_index - C_order index can be tracked
#f_index - Fortran_order index can be tracked
#multi-index - Type of indexes with one per iteration can be tracked
#external_loop - Causes values given to 1-D arrays with multiple values instead of 0-D array

a = np.arange(0,60,5)
a =a.reshape(3,4)

print('Original array is: ')
print(a)
print('\n')

print('Modified Array is: ')
for x in np.nditer(a,flags = ['external_loop'], order = 'F'):
	print(x)
print('\n')
print('\n')



#BROADCASTING ITERATION

#If two arrays are braoadcastable, a combined nditer obejct is able to iterate upon them concurrently.
#Assuming that an array a has dims 3X4, and there is another array b of dims 1X4,
#the iterator of the following type is used (array b is broadcast to size of a).

a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print('First array is: ')
print(a)
print('\n')

print('Second array is: ')
b = np.array([1,2,3,4], dtype = int)
print(b)
print('\n')

print('Modified array is: ')
for x,y in np.nditer([a,b]):
	print("%d:%d" % (x,y))
print('\n')
print('\n')


#ARRAY MANIPULATION

#CHANGING SHAPE: 

#reshape - Gives new shape to an array without changing its data 
#flat - A 1-D iterator over the array
#flatten - returns the copy of the array collapsed in one dimension
#ravel - returns contiguous flattened array

#TRANSPOSE OPERATIONS: 

#transpose - permutes the dimnsions of the array
#ndarray.T - same as self.transpose()
#rollaxis - rolls the specified axis backwards
#swapaxes - interchanges the two axes of an array

#CHANGING DIMENSIONS:

#broadcast - Produces an object that mimics broadcasting
#broadcast_to - broadcasts array to a new shape
#expand_dims - expands the shape of an array
#squeeze - Removes single dimensional entries from the shape of an array

#JOINING ARRAYS:

#concatenate - Joins a sequence of arrays along an existing axis
#stack - Joins a sequence of arrays along a new axis 
#hstack - Stacks arrays in sequence horizontally
#vstack - stacks arrays in sequence vertically

#SPLITTING ARRAYS: 

#split - splits an array into multiple sub-arrays
#hsplit - splits an arra into multiple sub arrays horizontally(column-wise)
#vsplit - splits an arra into multiple sub arrays vertically(row-wise)

#ADDING/REMOVING ELEMENTS: 

#resize - Returns a new array with the specified shape
#append - appends the values to the end of the array
#insert - Inserts the values to the end of an array
#delete - returns a new array with sub arrays along an axis deleted
#unique - finds the unique elements of an array* (WHAT UNIQUE????)



#NUMPY - BINARY OPERATORS

#bitwise_and - Computes bitwise AND operation of array elements
#bitwise_or - computes bitwise OR operation of array elements
#invert - computes bitwise NOT
#leftshift - shifts bits of a binary representaion to the left
#right_shift - shifts bits of binary representation to the right 



#NUMPY - STRING FUNCTIONS

#The following functions are used to perform vectorized string operations for arrays of 
#dtype numpy.string_ or numpy.unicode_ . They are based on the standard string functions in Python built in library

#add() - Returns element wise string concatenation for two arrays of str or unicode
#multiply() - returns the string with multiple concatenation, element wise
#center() -  returns the copy of the given string with elements centred ina a string of specified length
#capitalize() - returns a copy of the string with only the first character capitalized
#title() - returns the element wise title cased version of the string or unicode
#lower() - returns an array with elements converted to lowercase
#upper() - returns an array with the elements converted to uppercase
#split() - returns a list of words in the string, uing separator delimiter
#splitlines() - returns a list of lines in the element, breaking at the line boundaries
#strip() - returns a copy with the leading and trailing characters removed
#join() - returns a copy of the string with all occurences of substring replaced by new string
#decode() - calls str.decode element wise
#encode() - calls str.encode element wise 






 #MATHEMATICAL FUNCTIONS 

#Quite understandably, NumPy contains a large number of various mathematical operations.
#NumPy provides standard trigonometric functions, functions for arithmetic operations, handling complex numbers, etc.

#TRIGONOMETRIC FUNCTIONS - 

#Numpy has standard trigonometric functions which return the T-ratios for a given angle in radians.


a = np.array([0,30,45,60,90])
print(a)
print('\n')

#Convert angles into radians as follows - 

a = a*(np.pi/180)
print(a)
print('\n')

print('Sin values for the angles in the given array are: ')
print(np.sin(a))
print('\n')

print('Cos values for the angles in the given array are: ')
print(np.cos(a))
print('\n')

print('Tan values for the angles in the given array are: ')
print(np.tan(a))
print('\n')

print('Cot values for the angles in the given array are: ')
print(1/(np.tan(a)))
print('\n')

print('Sec values for the angles in the given array are: ')
print(1/(np.cos(a)))
print('\n')

print('Cosec values for the angles in the given array are: ')
print(1/(np.sin(a)))
print('\n')
print('\n')

#arcsin, arccos, arctan functions are used for inverse ratios

sine = np.sin(a)
print((np.arcsin(sine)*180)/np.pi)
print('\n')
#This gives us our original array. 
print('\n')

#or we could convert to degrees as- 

print(np.degrees(np.arcsin(sine)))
print('\n')



#FUNCTIONS FOR ROUNDING 

#numpy.around(a,decimals)
# a is input data, decimals is the number of decimals to round to. Default is 0.
# if decimals is negative, the integer is rounded to the left of the decimal point.

a = np.array([1.0,5.55,123,0.567,25.532])
print('Original array is: ')
print(a)
print('\n')

print('After rounding: ')
print(np.around(a))
print(np.around(a,decimals = 1))
print(np.around(a,decimals = -1))
print('\n')
print('\n')


#numpy.floor()
#This function returns the GIF or the greatest integer function of the given input
#The floor of scalar x, is the largest integer i, such that i<=x. Python always rounds flooring away from 0

a = np.array([-1.7, 1.5, -0.2, 0.6, 10])

print('The given array is: ')
print(a)
print('\n')

print('The modified array is: ')
print(np.floor(a))
print('\n')


#numpy.ceil()
#the ceil() function returns the ceiling of the input value. i.e the ceil of scalar 
#x is the smallest integer i, such that i >= x. 

a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 

print('The given array is: ')
print(a)
print('\n')

print('The modified array is: ')
print(np.ceil(a))
print('\n')
print('\n')




#ARITHMETIC OPERATIONS

#Input arrays for performing arithmetic operations such as add(), subtract(), 
#multiply(), and divide() must be either of the same shape or should conform to 
#array broadcasting rules.


a = np.arange(9, dtype = np.float_).reshape(3,3) 

print('First array:') 
print(a) 
print('\n')  

print('Second array:') 
b = np.array([10,10,10]) 
print(b) 
print('\n')  

print('Add the two arrays:') 
print(np.add(a,b)) 
print('\n')  

print('Subtract the two arrays:') 
print(np.subtract(a,b)) 
print('\n')  

print('Multiply the two arrays:') 
print(np.multiply(a,b)) 
print('\n')  

print('Divide the two arrays:') 
print(np.divide(a,b))
print('\n')



#numpy.reciprocal()

#This function returns the reciprocal of argument, element-wise. For elements 
#with absolute values larger than 1, the result is always 0 because of the way 
#in which Python handles integer division. For integer 0, an overflow warning is issued.



a = np.array([0.25, 1.333333, 1, 0, 100])

print('Our array is: ')
print(a)
print('\n')

print('After applying reciprocal: ')
print(np.reciprocal(a))
print('\n')

b = np.array([100],dtype = int)
print('The second array is: ')
print(b)
print('\n')

print('After applying reciprocal function: ')
print(np.reciprocal(b))
print('\n')
print('\n')




#numpy.power()

#This function treats the elements in the first input array as the base and returns 
#it raised to the power of the corresponding element in the second input array.

a = np.array([10,100,1000])

print('Our array is: ')
print(a)
print('\n')

print('Applying power function: ')
print(np.power(a,2))
print('\n')

print('Second array: ')
b = np.array([1,2,3])
print(b)
print('\n')

print('Applying Power function: ')
print(np.power(a,b))
print('\n')
print('\n')


#numpy.mod() or numpy.remainder()

#This function returns the remainder of division of the corresponding elements in the
#input array. The function numpy.remainder() also produces the same result.

a = np.array([10,20,30])
b = np.array([3,5,7])

print('First array: ')
print(a)
print('\n')

print('Second array: ')
print(b)
print('\n')

print('Applying remainder function: ')
print(np.remainder(a,b))
print('\n')
print('Mod function gives same result: ')
print(np.mod(a,b))
print('\n')
print('\n')



#FUNCTIONS FOR COMPLEX NUMBERS: 

#numpy.real() - returns the real part of the complex datat type argument
#numpy.imag() - returns the imaginary part of the complex data type argument
#nump.conj() - returns the complex conjugate, which is obtained by changing the sign of the imaginary part.
#nump.angle() - returns the angle of the complex argument. The function has degree parameter.
				#if true, the angle ing degree is returned, otherwise angle is in radians.


a = np.array([-5.6j, 0.2j, 4+3j, 7.1-2.4j])

print('Our array is: ')
print(a)
print('\n')

print('Applying real() function: ')
print(np.real(a))
print('\n')

print('Applying imag() function: ')
print(np.imag(a))
print('\n')

print('Applying conj() function: ')
print(np.conj(a))
print('\n')

print('Applying angle() function: ')
print(np.angle(a))
print('\n')

print('Applying angle() function (in degrees): ')
print(np.angle(a,deg = True))
print('\n')
print('\n')







#STATISTICAL FUNCTIONS


#numpy.amin() and numpy.amax() 

#These functions return the minimum and the maximum from the elements in the given array 
#along the specified axis

a = np.array([[3,7,5],[8,4,3],[2,4,9]])

print('Our array is: ')
print(a)
print('\n')

print('Applying amin() function: ')
print(np.amin(a,1))
print('\n')

print('Applying amin() function again: ')
print(np.amin(a,0))
print('\n')

print('Applying amax() function: ')
print(np.amax(a,1))
print('\n')

print('Applying amax() function again: ')
print(np.amax(a,0))
print('\n')
print('\n') 


#numpy.ptp()

#This function returns the range (maximum-minimum) of the values along an axis.

a = np.array([[3,7,5],[8,4,3],[2,4,9]])

print('Our array is: ')
print(a)
print('\n')

print('Applying ptp() function: ') #with no argument of axis, it gives range for entire array
print(np.ptp(a))
print('\n')

print('Applying ptp() function along axis 1: ')
print(np.ptp(a,axis = 1))
print('\n')

print('Applying ptp() function along axis 0: ')
print(np.ptp(a,axis = 0))
print('\n')
print('\n')


#numpy.percentile() 

#Percentile (or a centile) is a measure used in statistics indicating the value below which a 
#given percentage of observations in a group of observations fall. 
#The function numpy.percentile() takes the following arguments.


#numpy.percentile(a, q, axis)


#a - input array
#q - the percentile to compute (must be between 0 and 100)
#axis - the axis along which percentile is to be caculated

print('Our array is:') 
print(a) 
print('\n')  

print('Applying percentile() function:') 
print(np.percentile(a,50)) 
print('\n')  

print('Applying percentile() function along axis 1:') 
print(np.percentile(a,50, axis = 1)) 
print('\n')  

print('Applying percentile() function along axis 0:') 
print(np.percentile(a,50, axis = 0))
print('\n')
print('\n')



#numpy.median() 

#Median is defined as the value separating the higher half of a data smaple from the lower half. 
#The numpy.median() function is used as shown in the following - 


a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 

print('Our array is:') 
print(a)
print('\n')  

print('Applying median() function:' )
print(np.median(a)) 
print('\n')  

print('Applying median() function along axis 0:') 
print(np.median(a, axis = 0)) 
print('\n')  
 
print('Applying median() function along axis 1:') 
print(np.median(a, axis = 1))
print('\n')



#numpy.mean()

#Don't tell me you didn't see it coming! Still here is the def for noobs- 
#Arithmetic mean is the sum of elements along an axis divided by the number of elements. 
#The numpy.mean() function returns the arithmetic mean of elements in the array. 
#If the axis is mentioned, it is calculated along it.


a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print('Our array is:') 
print(a) 
print('\n')  

print('Applying mean() function:') 
print(np.mean(a)) 
print('\n')  

print('Applying mean() function along axis 0:') 
print(np.mean(a, axis = 0)) 
print('\n')  

print('Applying mean() function along axis 1:') 
print(np.mean(a, axis = 1))
print('\n')
print('\n')


#Now here things get a bit more... whatever...


#numpy.average()

#Weighted average is an average resulting from the multiplication of each component 
#by a factor reflecting its importance.The numpy.average() function computes the weighted
# average of elements in an array according to their respective weight given in another array. 
#The function can have an axis parameter. 
#If the axis is not specified, the array is flattened.

#Considering an array [1,2,3,4] and corresponding weights [4,3,2,1], the weighted average 
#is calculated by adding the product of the corresponding elements and 
#dividing the sum by the sum of weights.

#Weighted average = (1*4+2*3+3*2+4*1)/(4+3+2+1)

a = np.array([1,2,3,4])

print('Our array is: ')
print(a)
print('\n')

print('Applying average() function: ')
print(np.average(a))
print('\n')
#this was the same case as when weighted average is not specified.

wts = np.array([4,3,2,1])

print('Applying average() function again: ')
print(np.average(a,weights = wts))
print('\n')

#Returns the sum of weights if the returned parameter 'returned' is set to true
print('Sum of weights: ')
print(np.average([1,2,3,4],weights = [4,3,2,1], returned = True ))
print('\n')
print('\n')

#In a multi-dimensional array, the axis for computation can be specified.

a = np.arange(6).reshape(3,2) 

print('Our array is:') 
print(a) 
print('\n')  

print('Modified array:') 
wt = np.array([3,5]) 
print(np.average(a, axis = 1, weights = wt)) 
print('\n')  

print('Modified array:') 
print(np.average(a, axis = 1, weights = wt, returned = True))
print('\n')
print('\n')



#STANDARD DEVIATION

#Standard deviation is the square root of the average of the squared deviations from mean.
#The formula for the standard deviation is like this: 

#		std = sqrt(mean(abs(x - x.mean())**2))

#to print standard deviation of data from an array: 

print(np.std([1,2,3,4]))
print('\n')


#VARIANCE

#Standard Deviation is the square of variance. Hence remove the sqrt function in the def. to get formula

print(np.var([1,2,3,4]))
print('\n')




#NUMPY - SORT, SEARCH AND COUNTING FUNCTIONS



#The follwing types of sorting algortihms and their charcterestics can be implemented.


# quicksort - Speed = 1, worst case = O(n^2), workspace = 0, stable = no

# mergesort - Speed = 2, worst case = O(n*(log(n))), workspace = ~n/2, stable = yes

# heapsort - Speed = 3, worst case = O(n*(log(n))), workspace = 0, stable = no



#  numpy.sort(a, axis, kind, order)

#a - Array to be sorted
#axis - The axis along which the array is to be sorted. If none, the array is flattened, sorting on the last axis. 
#kind - Default is quicksort
#order - If the array conatins fields, the order of the fields to be sorted.

a = np.array([[3,7],[9,1]])

print('Our array is: ')
print(a)
print('\n')

print('Applying sort() function: ')
print(np.sort(a))
print('\n')

print('Sort along axis 0: ')
print(np.sort(a, axis=0))
print('\n')

#order parameter in sort function: 

dt = np.dtype([('name', 'S10'),('age', int)])
a = np.array([('zeus' , 21),('poseidon', 25),('palla', 43),('legend', 999)], dtype = dt)

print('Our array is: ')
print(a)
print('\n')

#Order by name: 
print('Order by name: ')
print(np.sort(a, order = 'name'))
print('\n')






# numpy.argsort()

# This function performs an indirect sort on an input array, along the given axis and using
# a specified kind of dort to return the array of indices of data.
#This indices array is used to construct the sorted array. 


x = np.array([3,1,2])

print('Our array is: ')
print(x)
print('\n')

print('Applying argsort() to x: ')
y = np.argsort(x)
print(y)
print('\n')

print('Reconstruct original array in sorted order: ')
print(x[y])
print('\n')

print('Reconstruct the original array using loop: ')
for i in y:
	print(x[i])
print('\n')
print('\n')




#numpy.lexsort()

#This function performs an indirect sort using a sequence of keys. 
#The keys can be seen as a column in a spreadsheet. 
#The function returns an array of indices, using which the sorted data can be obtained. 
#Note, that the last key happens to be the primary key of sort.


nm = ('raju','anil','ravi','amar') 	#Tuple 1
dv = ('f.y.', 's.y.', 's.y.', 'f.y.') 


ind = np.lexsort((dv,nm)) 


print('Applying lexsort() function: ')
print(ind)
print('\n')

print('Use this index to get sorted data: ')
print([nm[i] + ", " + dv[i] for i in ind])
print('\n')
print('\n')




#numpy.argmax() and numpy.argmin(): 

#These two functions return the indices of the max and min elements respectively along the axis
#It searches within the array.


#take an array: 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

print('Our array is: ')
print(a)
print('\n')

print('Applying argmax() function: ')
print(np.argmax(a))
print('\n')

print('Index of max value in flattened array: ')
print(a.flatten())
print('\n')

print('Array containing indices of maximum along axis 1: ')
maxindex = np.argmax(a, axis = 1)
print(maxindex)
print('\n')

print('Array containing indices of maximum along axis 0: ')
maxindex = np.argmax(a, axis = 0)
print(maxindex)
print('\n')

print('Applying argmin() function: ')
minindex = np.argmin(a)
print(minindex)
print('\n')

print('Flattened array: ')
print(a.flatten()[minindex])
print('\n')

print('Flatened array along axis 0: ')
minindex = np.argmin(a, axis = 0)
print(minindex)
print('\n')

print('Flattened array along axis 1: ')
minindex = np.argmin(a, axis = 1)
print(minindex)
print('\n')


#numpy.nonzero()

#This function returns the indices of the nonzero elements in the array.

a = np.array([[30,40,10],[0,20,10],[50,0,60]])

print('Our array is: ')
print(a)
print('\n')

print('Applying nonzero() function: ')
print(np.nonzero(a))
print('\n')



#numpy.where()

#This function returns the indices of the elements in an input array where the given condition is satisfied


x = np.arange(9.).reshape(3, 3)

print('Our array is: ')
print(x)
print('\n')

print('Indices of elements > 3: ')
y = np.where(x > 3)
print(y)
print('\n')

print('Use these indices to get elements satisfying the condition ')
print(x[y])
print('\n')



#numpy.extract()

#This function returns the elements satisfying any condition: 

x = np.arange(9.).reshape(3,3)

print('Our array is: ')
print(x)
print('\n')

#define a condition
condition = np.mod(x,2) == 0

print('Element wise value of condition: ')
print(condition)
print('\n')

print('Extract elements using condition: ')
print(np.extract(condition,x))







#NUMPY BYTE-SWAPPING

#numpy.ndarray.byteswap()

#This function toggles between the two representations- bigendian and little-endian.
#These two are the ways on how data is stored in the memeory depending upon the architecture of the CPU.

# Little-endian - least significant is stored in the smallest address
#Big-endian - Most significant byte in the smallest address

a = np.array([1,256,8755], dtype = np.int16)

print('Our array is: ')
print(a)
print('\n')

print('Representation of data in memory in hexadecimal form: ')
print(map(hex,a))
print('\n')

#byteswap() function swaps in place by passing the True parameter

print('Applying byteswap() function: ')
print(a.byteswap(True))
print('\n')

print('In hexadecimal form: ')
print(map(hex,a))
print('\n')




#COPIES AND VIEWS : 

#While executing the functions, some of the functions return a copy of the input array,
#while others return the view. When the contents are physically stored in another location, it is called a COPY
#If a different view of the same memory content is provided, we call it as a VIEW

#NO COPY

#Simple assignments do not make the copy of the array object. Instead uses the same id() of the original array to access it.
# The id() returns the universal identifier of Python object, similar to the pointer in C.

#Any changes in either gets reflected in the other. For example the changing shape of one changes that of the other.

a = np.arange(6)

print('Our array is: ')
print(a)
print('\n')

print('Applying id() function: ')
print(id(a))
print('\n')

print('b is assigned to a')
b = a
print('\n')

print('b has the same id(): ')
print(id(b))
print('\n')

print('Change shape of b: ')
b.shape = (3,2)
print(b)
print('\n')

print('Shape of a also gets changed: ')
print(a)
print('\n')




#VIEW OR SHALLOW COPY

#Numpy has ndarray.view() method which is new array object that looks at the same data of the original array. 
#Unlike the earlier case, change in dimensions of the new array doesn't change the dims of the original.


a = np.arange(6).reshape(3,2)

print('Array a: ')
print(a)
print('\n')

print('Create view of a: ')
b = a.view()
print(b)
print('\n')

print('id() for both the arrays are different: ')
print('id() of a: ')
print(id(a))
print('id() of b: ')
print(id(b))
print('\n')

#Change the shape of b. It does not change the shape of a
b.shape = (2,3)

print('Shape(a): ')
print(a)
print('Shape(b): ')
print(b)
print('\n')




a = np.array([[10,10],[2,3],[4,5]])

print('Our array is: ')
print(a)
print('\n')
print('Create a slice: ')
s = a[:, :2]
print(s)
print('\n')



#DEEP COPY 

#The ndarray.copy() function creates a deep copy. It is a complete copy of array and data.
#It doesn't share the original array. 

a = np.array([[10,20],[2,3],[4,5]])

print('Array is: ')
print(a)
print('\n')

print('Create a deep copy of a: ')
b = a.copy()
print('Array b is: ')
print(b)
print('\n')

#b does not share any memory with a.
print('Can we write "b is a"? : ')
print(b is a)
print('\n')

print('Change the contents of b: ')
b[0,0] = 100

print('modified array b: ')
print(b)

print('a remains unchanged: ')
print(a)
print('\n')



#NUMPY MATRIX LIBRARY

#Numpy contains a libraru numpy.matlib
# This module has functions that return matrices instead of ndarray objects.


#matlib.empty()

#The matlib.empty() function returns a new matrix without initializing the entiries. 


# numpy.matlib.empty(shape, dtype, order)

#shape - int or tupe of int defining the shape of the new matrix
#dtype - Optional. Data type of the output.
#order - C or F

import numpy.matlib
import numpy as np

print(np.matlib.empty((2,2)))
print('\n')

#numpy.matlib.zeros()
print(np.matlib.zeros((2,2)))
print('\n')

#numpy.matlib.ones()
print(np.matlib.ones((2,3)))
print('\n')


#numpy.matlib.eye() 
#This functions returns 1 along the diagonals and zeros elsewhere.

#numpy.matlib.eye(n,M,k,dtype)

#n - Number of rows in the resulting matrix
#M - Number of columns, defaults to n
#k - Index of diagonal
#dtype - Data type of the output

import numpy.matlib
import numpy as np 
print(np.matlib.eye(n = 3,M = 4, k = 0, dtype = float))
print(np.matlib.zeros((2,2)))
print('\n')



#numpy.matlib.identity()

#The numpy.matlib.identity() function returns the Identity matrix of the given size. 
#An identity matrix is a square matrix with all diagonal elements as 1.

import numpy.matlib 
import numpy as np 
print(np.matlib.identity(5, dtype = float))
print('\n')


#numpy.matlib.rand() 

#The numpy.matlib.rand() function returns a matrix of the given size filled with random values

import numpy.matlib 
import numpy as np 
print(np.matlib.rand(3,3))
print('\n')
































