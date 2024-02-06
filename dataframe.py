import pandas as pd
import random
def number(a, string):
    if a == string:
        n = 1
    else:
        n = 0
    return n
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
lst21 = [number(item, 'robot') for item in lst]
lst22 = [number(item, 'human') for item in lst]
data = pd.DataFrame({'Robot':lst21})
data['Human'] = lst22
print(data)
