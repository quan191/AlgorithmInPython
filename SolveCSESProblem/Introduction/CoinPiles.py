t=int(input())
for i in range (0,t):
    test_list=input().split(" ")
    y=int(test_list[0])
    x=int(test_list[1])
    if (x+y)%3==0:
        if (x==0 and y==0):
            print("YES")
        elif(x==0 or y==0):
            print("NO")
        else:
            m=((y+x)//3)+y-x
            
            if(m%2==0 ):
                n=y-m
                if(n>=0 and m>=0):
                    print("YES")
                else :
                    print("NO")
            else :
                print("NO")
    else: 
        print("NO")
