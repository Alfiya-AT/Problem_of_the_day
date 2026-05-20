def Modify(arr):
    j=0
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            arr[j]=arr[i-1]*2
            arr[i]=0
            i+=1
            j+=1
        elif arr[i]!=0:
            arr[j]=arr[i]
            arr[i]=0
            j+=1
            i+=1
    left=0
    right=0       
    while left<right:
        if left
    return arr

arr=[2,2,0,4,0,8]
print(arr)
print(Modify(arr))
# Output: [4, 4, 8, 0, 0, 0] 