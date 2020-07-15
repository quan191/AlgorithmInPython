n=int(input())
if n%4==3:
    print("YES")
    x=n//4
    list1=[1,2]
    list2=[3]
    for i in range(1,x+1):
        list1.append(4*i)
        list1.append(4*i+3)
        list2.append(4*i+1)
        list2.append(4*i+2)
    print(len(list1))
    for i in list1:
        print(i,end=" ")
    print()
    print(len(list2))
    for i in list2:
        print(i,end=" ")
elif n%4==0:
    print("YES")
    x=n//4
    list1=[]
    list2=[]
    
    for i in range(0,x):
        m=4*i
        list1.append(m+1)
        list1.append(m+4)
        list2.append(m+2)
        list2.append(m+3)
    print(len(list1))
    for i in list1:
        print(i,end=" ")
    print()
    print(len(list2))
    for i in list2:
        print(i,end=" ")
else :
    print("NO")