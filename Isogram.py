def Isogram (s = "machine"):
    
    # best case < n due to early exit 🚀
    seen = set()
    for ch in s:
        if ch in seen:
            return False   # duplicate found immediately
        seen.add(ch)
    return True
    
    
    # d={}
    # for i in s:
    #     d[i]=d.get(i,0)+1
    # for key,value in d.items():
    #     if value>1:
    #         return False
    # return True

print(Isogram())