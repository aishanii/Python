import numpy as num
arr1=num.array([1,2,3])
arr2=arr1.copy()

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

#deep copy
#two arrays not linked in any way