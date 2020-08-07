def BinarySearch(arr,l,r,x):
    if r<l:
        return False
    mid=l+(r-l)//2
    if arr[mid]>x:
        return BinarySearch(arr,l,mid-1,x)
    elif arr[mid]<x:
        return BinarySearch(arr,mid+1,r,x)
    else:
        return True

arr=[1,5,6,7,8]
k=BinarySearch(arr,0,len(arr)-1,8)
print(k)