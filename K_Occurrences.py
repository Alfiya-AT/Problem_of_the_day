def occurrences(arr,k):
    d={}
    for i in range(len(arr)):
        d[arr[i]]=d.get(arr[i],0)+1 
        if d.get(arr[i])>=k:
            return arr[i]
    
    return -1

arr= [1, 8, 2, 1]
k = 2
# Output: 4
print(occurrences(arr,k))