def LengthEncoding(s):
    ans=''
    i=0
    while i<len(s):
        cnt=0
        j=i
        ans+=s[i]
        while j<len(s) and s[i]==s[j] :
            cnt+=1
            j+=1
        i=j
        ans+=str(cnt)
    return ans

s = 'abbbcdddd'
# Output: a1b3c1d4
# s = 'aaaabbbccc'
# Output: a4b3c3
print(LengthEncoding(s))