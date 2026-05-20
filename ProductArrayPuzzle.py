# def productExceptSelf(arr):
    # n=len(arr)
    # left=0
    # right=len(arr)-1
    # l=[]
    # r=[]
    # res=[]
    # x=1
    # y=1
    # while left<n:
    #     l.append(x)
    #     x*=arr[left]
    #     left+=1
    # print(l)

   
    # while right>-1:
    #     r.append(y)
    #     y*=arr[right]
    #     right-=1
    # print(r)
    
    # i=0
    # j=len(arr)-1
    # while i<len(arr) and j>-1:
    #     res.append(l[i]*r[j])
    #     i+=1
    #     j-=1
    # return res

def productExceptSelf(arr):
    res=[]
    n=len(arr)
    i=0
    res=[]
    x=y=1
    while i<n:
        res.append(x)
        x*=arr[i]
        i+=1
    print(res)
    i-=1
    while i>-1:
        res[i]*=y
        y*=arr[i]
        i-=1
    print(res)   
    return res

    
    return res
arr= [10, 3, 5, 6, 2]

print(productExceptSelf(arr))
# Output: [180, 600, 360, 300, 900]