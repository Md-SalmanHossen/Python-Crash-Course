
# numpy: dimensional
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
print("1d : \n",arr1)

arr2=np.array([[1,2,3],[4,5,6]])
print("2d: \n",arr2)

# access through row and column: 
print(arr2[1][0])

print("Dimensions : ",arr2.ndim)
print("Dimensions : ",arr2.shape)
print("Dimensions : ",arr2.size)
print("Dimensions : ",arr2.dtype)




