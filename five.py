#to check if a number is present in a list
def is_available(list,n):
   for i in list:
       if n == i:
           return True
   return False

print(is_available([1, 5, 8, 3], 3))
print(is_available([5, 8, 3], -1))
