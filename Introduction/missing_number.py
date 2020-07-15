

n=int(float(input()))
test_list=input().split(' ')
test_list = list(map(int, test_list)) 
sumN=n*(n+1)/2
print(int(sumN)-sum(test_list))


