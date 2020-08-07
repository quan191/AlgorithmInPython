list1=[int(x) for x in input().split(' ')]
n=list1[0]
k=list1[1]
list2=[int(x)for x in input().split(' ')]
list2.sort()
sum=0
i=0
j=len(list2)-1
while(i<j):
    if list2[i]+list2[j]<=k:
        i+=1
        j-=1
        sum+=1
    elif list2[j]>k:
        j-=1
    else:
        j-=1
        sum+=1
if i==j and list2[i]<k:
    sum+=1
print(sum)
