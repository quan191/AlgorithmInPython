t=int(input())
for i in range (0,t):
  test_list=input().split(" ")
  y=int(test_list[0])
  x=int(test_list[1])
  maxNum=max(y,x)
  if maxNum%2==0:
    if maxNum==x:
      result=(maxNum-1)**2+y
    else :
      result=maxNum**2-x+1
  else :
    if maxNum==x:
      result=maxNum**2-y+1
    else :
      result=(maxNum-1)**2+x
  print(result)