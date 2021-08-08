#selecting random elements from dictionary

import random


d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key]) 


