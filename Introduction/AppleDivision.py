n=int(input())
test_list=input().split(' ')
test_list=list(map(int,test_list))
x=sum(test_list)

def minimum(s, ls):
    if len(ls) == 1:
        return abs(s - 2*ls[0])
    else:
        m =abs(s - 2*ls[0])
        for i in range(1,len(ls)):
            m = min(m,abs(minimum(s - 2*ls[i], ls[:i])))
        return m

print(minimum(x,test_list))


        