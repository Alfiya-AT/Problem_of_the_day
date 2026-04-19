def Repeated(s ="geeksforgeeks"):
    # use set bcz it take less time  O(n) for searching while lsit do linear search n it takes O(n*n)
    res=set()
    for i in range(len(s)):
        if s[i] not in res:
            res.add(s[i])
        else:
            return s[i]
    return -1
print(Repeated())