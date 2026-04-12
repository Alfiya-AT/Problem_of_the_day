def CountElements(a,b,n,query,q):
    cnt=0
    p=0
    res=[]
    for i in a:
        cnt=0
        for j in b:
            if j<=i:
                cnt+=1
        res.append(cnt)
        p+=1
        if p==q:
            break


    return res




n = 3
a= {4,1,2}
b= {1,7,3}
q = 2
query= {0,1}
# Output : 
# 2
# 1
print(CountElements(a,b,n,query,q))