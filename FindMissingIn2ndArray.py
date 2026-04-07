def findMissing(a,b):
    res=[]
    b=set(b)
    for i in a:
        if i not in b:
            res.append(i)
    return res

a=[1, 2, 3, 4, 5, 10]
b=[2, 3, 1, 0, 5]
# Output: [4, 10]
print(findMissing(a,b))