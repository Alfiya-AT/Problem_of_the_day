def wifi( N, S, X):
    prev=-1
    for i in range(N):
        if S[i]=='1':
            if prev==-1:
                if i>X:
                    return 0

            else:
                if i-prev>(2*X+1):
                    return 0

            prev=i

    if prev==-1:
        return 0

    if(N-1-prev)>X:
        return 0

    return 1

print(wifi( N=5, X=1, S="100010"))
