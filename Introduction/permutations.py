n=int(input())
if (n==1):
    print(1)
if (n==2 or n==3):
    print("NO SOLUTION")
else : 
    if (n%2==0):
        i=2
        k=1
    else :
        i=1
        k=2
    while (i<=n):
        print(i)
        i+=2
    while (k<n):
        print(k)
        k+=2