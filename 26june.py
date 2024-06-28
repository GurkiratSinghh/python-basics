#fetching the first element
import numpy as np 
arr=np.array([1,2,3,4,5])
print(arr[0])

##fetching the second element
import numpy as np 
arr=np.array([1,2,3,4,5])
print(arr[1])

##fetching the third and fourth element and add them
import numpy as np 
arr=np.array([1,2,3,4,5])
print(arr[2]+arr[3])

#Access the element on the first row, second column:
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

#Access the element on the second row, fifth column:
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("5th element from 2nd row:",arr[1,4])

# Access the third element of the second array of the first array
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# Negative indexing
#Print the last element from the 2nd dim:

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[-1, -1])

#Slice elements from index 1 to index 5 from the following array:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Slice elements from index 4 to the end of the array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

#Slice elements from the beginning to index 4 (not included):
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

#Slice from the index 3 from the end to index 1 from the end:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

#Use the step value to determine the step of the slicing:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

#Return every other element from the entire array:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

#From the second element, slice elements from index 1 to index 4 (not included):
import numpy as np
arr = np.array([[1, 2, 3, 4,5,6], [5, 6, 7,8,9,10]])
print(arr[1,1:4])

#From both elements, return index 2:
#if i want element from both arrays
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2,2])


# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2,1:4])

