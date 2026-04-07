# Find (target - i) in arr2

def allPairs(target, a, b):
    d={}
    for i in b:
        d[i]=d.get(i,0)+1
    res=[]
    a.sort()
    
    for i in a:
        needed=target-i
        if needed in d:
            
            count=d[needed]
            res.extend([[i,needed]]*count)
    return res

target = 8
a = [-1, -2, 4, -6, 5, 7] 
b = [6, 3, 4, 0]
print(allPairs(target, a, b))