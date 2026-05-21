def Modify(arr):
    right=1

    while right<len(arr):
        left=right-1
        if arr[left] == arr[right]:
            arr[left]=2*arr[left]
            arr[right]=0
            right+=2
        else:
            right+=1
    j=0
    count=0
    for i in range(len(arr)):
        if arr[i]>0:
            arr[j]=arr[i]
            j+=1
    while j<len(arr):
        arr[j]=0
        j+=1
    return arr


arr = [2, 2, 0, 4, 0, 8]
print(arr)
print(Modify(arr))