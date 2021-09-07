import numpy as num
arr1=num.array([1,2,3])
arr2=arr1.view() #shallow copy
print(arr1)
print(arr2)

#both are still dependent on each other