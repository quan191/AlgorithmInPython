test_list=[]
k=[[c=='*' for c in input()]for j in range(8)]
not_Pick1=[False]*15
not_Pick2=[False]*15
colum=[False]*8
sum=0
def solve(i):
    global sum,colum,not_Pick1,not_Pick2,k
    if i==8:
        sum+=1
    for j in range (0,8):
        if(colum[j]==True or not_Pick1[j+i]==True or not_Pick2[7-j+i]==True or k[i][j]==True ):
            continue
        colum[j]=True
        not_Pick1[j+i]=True
        not_Pick2[7-j+i]=True
        solve(i+1)
        not_Pick1[j+i]=False
        not_Pick2[7-j+i]=False
        colum[j]=False
    
solve(0)
print(sum)