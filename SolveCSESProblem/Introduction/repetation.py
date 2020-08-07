string=input()
max=0
i=0
while (i<len(string)):
    repe=1
    for j in range (i+1,len(string)):
        if string[i]==string[j]:
            repe+=1
        else :
            break
    if repe>max :
        max=repe
    i=i+repe
print(max)