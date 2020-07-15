
k=input()
check=[[True for i in range(9)]for j in range(9)]
for i in range(9):
    check[0][i]=False
    check[i][0]=False
    check[8][i]=False
    check[i][8]=False
sum=0
def solve(i,j,m):
    if (i==7 and j==1):
        if m==48:
            global sum
            sum+=1
            return 0
    check[i][j]=False
    if (k[m]=='?'):
        if check[i-1][j]:
            solve(i-1,j,m+1)
        if check[i][j-1]:
            solve(i,j-1,m+1)
        if  check[i][j+1]:
            solve(i,j+1,m+1)
        if check[i+1][j]:
            solve(i+1,j,m+1)
        check[i][j]=True
        return 0
    else:
        if (k[m]=='D' and check[i+1][j]==True):
            solve(i+1,j,m+1)
        if (k[m]=='L' and check[i][j-1]==True):
            solve(i,j-1,m+1)
            
        if (k[m]=='U' and check[i-1][j]==True):
            solve(i-1,j,m+1)
            
        if (k[m]=='R' and check[i][j+1]==True):
            solve(i,j+1,m+1)
        check[i][j]=True
        return 0
        
solve(1,1,0)
print(sum)