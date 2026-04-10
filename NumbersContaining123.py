def NumbersContaining123(arr):

    # TC : O(n)
    res=[]
    val=[1,2,3]
    for i in arr:
        p=0
        num=i
        while num>0:
            if (num%10) not in val:
                p=0
                break
            else:
                p=1
            num//=10
        if p==1:
            res.append(i)
            
    return res if len(res)>0 else [-1]



arr = [4, 6, 7, 12]
# Output: [-1]
print(NumbersContaining123(arr))