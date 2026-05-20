def Segregate(arr):
    # O(n)+O(n)
    # cnt=0
    # for i in arr:
    #     if i==0:
    #         cnt+=1
    # j=0
    # while j<cnt:
    #     arr[j]=0
    #     j+=1
    # while j<len(arr):
    #     arr[j]=1
    #     j+=1



    #   or best approach 

    # O(n)
    i=j=0
    for i in range(len(arr)):
        if arr[i]==0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
        
    return arr

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]

# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

print(Segregate(arr))