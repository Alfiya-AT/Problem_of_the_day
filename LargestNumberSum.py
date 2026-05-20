def Largestnumber(N,S):
    # res=0
    # val=9*N
    # if S<=val:
    #     div=(S)//9
    #     rem=(S)%9
    #     while div>0:
    #         res=res*10+9
    #         div-=1
    #     if len(str(res))<N:
    #         res=res*10+rem
    #     while len(str(res))<N:
    #         res=res*10
            
    # else:
    #     return -1
    # return res

# ----------------------------------------------.
    res=''
    l=0
    val=N*9
    if S<=val:
        while S>0:
            rem=min(9,S)
            res += str(rem)
            l+=1
            S=S-9
            print(res)
        while l<N:
            res+='0'
            l+=1
            
        
    else:
        return -1
    return res

N = 4
S = 12
# Output: 93000
print(Largestnumber(N,S))
# =>20000   