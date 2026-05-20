def countzero(arr):
    cnt=0
    arr.sort()
    i=0
    
    while i<len(arr):
        if arr[i]==0:
            cnt+=1
        i+=1
    return cnt
# arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
# Output: 3
arr=[0,0,0,0]
print(countzero(arr))