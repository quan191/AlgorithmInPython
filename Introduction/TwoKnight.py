n=int(input())
for i in range (1,n+1):
    atkPosition=4*(i-1)*(i-2)
    m=i**2
    position=int(m*(m-1)/2)
    print((position-atkPosition))