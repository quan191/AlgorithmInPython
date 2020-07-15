n=int(input())
test_list=input().split(" ")
test_list=list(map(int,test_list))
sumary=0
for i in range (1,len(test_list)):
    if test_list[i-1]-test_list[i]>0 :
         sumary= sumary + test_list[i-1]-test_list[i] 
         test_list[i]=test_list[i-1]
print(sumary)