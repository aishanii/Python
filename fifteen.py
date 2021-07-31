#to find the maximum and minimum numbers in a given list

def max_min(lst):
    min=lst[0]
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
        elif i<min:
            min=i
    return max,min

print(max_min([15,12,3,8]))

