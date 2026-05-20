def NonRepeating(arr):
    d={}
    for i in range(len(arr)):
        d[arr[i]]=d.get(arr[i],0)+1
    for key,value in d.items():
        if value==1:
            return key
    return 0

arr = [-1, 2, -1, 3, 2]
print(NonRepeating(arr))
# Output: 3
