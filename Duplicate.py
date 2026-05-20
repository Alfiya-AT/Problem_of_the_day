def duplicate(arr):
    # res=[]
    # for i in arr:
    res=list(set(arr))

    return res

arr= [2, 2, 3, 3, 7, 5] 
# Output: [2, 3, 7, 5]
print(duplicate(arr))