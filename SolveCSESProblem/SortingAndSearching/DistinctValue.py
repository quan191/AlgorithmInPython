n=int(input())
test_list=[int(x) for x in input().split(' ')]
hash_map={}
for i in test_list:
    hash_map[i]='Yes'
print(len(hash_map))

