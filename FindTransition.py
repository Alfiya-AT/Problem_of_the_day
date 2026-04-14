from turtle import right


def Find(arr):
    # idx=-1
    # cnt=0
    # i=0
    # if sum(arr)==0:
    #     return -1
    # elif sum(arr)==len(arr):
    #     return 0
    # else:
    #     while arr[i]!=1:
    #         i+=1
    #     return i


    l=0
    r=len(arr)-1
    ans=-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==1:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans

arr = [0, 0, 0, 1, 1]
# Output: 3
print(Find(arr))