def index(a,b):
    l=0
    r=len(b)-1
    while l<=r:
        mid=(l+r)//2
        if a[mid]==b[mid]:
            l=mid+1
        else:
            r=mid-1
    return l
a = [2,4,6,8,9,10,12]
b = [2,4,6,8,10,12]
print(index(a,b))
# Output: 4