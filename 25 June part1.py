# 0-d Array 
import numpy as np
arr=np.array(42)
print((arr))

#1-d Array
import numpy as np
arr=np.array([1,2,3,4])
print(arr)

#2-D Array
import numpy as np
arr=np.array([[1,2,3,4],(5,6,7,8)])
print(arr)

#3-D array
import numpy as np 
arr=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print(arr)

#check dimensions
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher dimensional array
import numpy as np
arr=np.array([[1,2,3,4,5]],ndmin=5)
print(arr)
print("Number of dimensions: ",arr.ndim)
