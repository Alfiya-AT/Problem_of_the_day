def intersection(arr1,arr2):
    res=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]==arr2[j]:
            res.append(arr1[i])

            while i<len(arr1)-1 and arr1[i]==arr1[i+1] :
                i+=1
            while j<len(arr2)-1 and arr2[j]==arr2[j+1] :
                j+=1
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
    return res


arr1= [1, 2, 2, 3, 4]
arr2= [2, 4, 6, 7, 8]
# Output: [2, 4]
print(intersection(arr1,arr2))