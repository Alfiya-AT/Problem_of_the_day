def find_index(arr,key):
    res=[-1,-1]
    n=len(arr)
    l=0
    r=n-1
    while l<n and r>-1 :
        if arr[l]==key and res[0]<0:
            res[0]=l
        if res[1]<0 and arr[r]==key:
            res[1]=r
        l+=1
        r-=1
    return res

 
arr = [1, 2, 3, 4, 5, 5] 
key = 5
print(find_index(arr,key))
# Output:  [4, 5]