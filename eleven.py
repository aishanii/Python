
#to print a list of numbers divisible by a number
lst=[15,30,67,4]
res=list(filter(lambda x:(x%15==0),lst))
print(res)