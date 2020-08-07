list1=[int(x) for x in input().split(' ')]
list2=[int(x) for x in input().split(' ')]
list3=[int(x) for x in input().split(' ')]
list2.sort()
list3.sort()
sum=0
i=j=0
while (i<len(list2) and j <len(list3)):
    if (list2[i]>=list3[j]-list1[2] and list2[i]<=list3[j]+list1[2]):
        sum+=1
        i+=1
        j+=1
    elif list2[i]>list3[j]:
        j+=1
    else:
        i+=1
print(sum) 