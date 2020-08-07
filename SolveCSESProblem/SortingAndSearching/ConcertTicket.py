list1=[int(x) for x in input().split(' ')]
list2=[int(x) for x in input().split(' ')]
list3=[int(x) for x in input().split(' ')]
n=list1[0]
m=list2[1]
hash_table={}
list2.sort()
for i in list2:
    if i not in hash_table.keys():
        hash_table[i]=1
    else:
        hash_table[i]+=1

j=0
a=0
print(hash_table)
while(j!=m):
    k=-1
    for i in hash_table.keys():
        if i<list3[j]:
            a=i
            continue
        hash_table[a]-=1
        k=a
    j+=1
    print(k)
