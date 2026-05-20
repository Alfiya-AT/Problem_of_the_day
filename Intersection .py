def Intersection(a,b):
    cnt=0
    a=set(a)
    b=set(b)
    for i in a:
        if i in b:
            cnt+=1
    return cnt
a = [89, 2, 75, 11, 23]
b = [89, 2, 2]
print(Intersection(a,b))