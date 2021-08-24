#to calculate the frequency of chars 

def char_freq(str):
    dict={}

    for n in str:
        keys=dict.keys()

        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_freq('aishani'))

