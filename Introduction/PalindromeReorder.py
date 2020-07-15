def reverse(string): 
    string = "".join(reversed(string)) 
    return string

n=input()
dict={}
for i in n:
    if i in dict.keys():
        dict[i]=dict[i]+1
    else:
        dict[i]=1
check=0
for key in dict.keys():
    if dict[key]%2==1 :
        check+=1

if check>1 :
    print("NO SOLUTION")
else :
    x=''
    y=''
    z=''
    for key in dict.keys():
        if dict[key]%2==0:
            x=x+key*(dict[key]//2)
            y=y+key*((dict[key]+1)//2)
        else:
            z=z+key*dict[key]

    print(x+z+reverse(y))

    
