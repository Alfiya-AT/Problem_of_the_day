def CountElements(a,b,n,query,q):
    res=[]
    for i in query:
        print("i",i)
        val1=list(a)[i]
        print(f"val=> {val1}")
        cnt=0
        for j in b:
            print(j)
            if j<=val1:
                cnt+=1
                print(f"cnt{cnt}")
        print()    
        res.append(cnt)
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