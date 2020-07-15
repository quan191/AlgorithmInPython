from itertools import permutations 
import string
s=input()
pre_list=permutations(s)
result=[]
dict={}
for i in pre_list:
    dict[i]=i
for i in dict.keys():
    result.append(i)
result.sort()
print(len(result))
for i in result:
    print(''.join(i))