def licenseKeyFormatting(s,k):
    s=s.replace("-","")
    if len(s)<k:
        return s
    rem=0
    res=""
    if len(s)%k!=0:
        rem=len(s)%k
        res+=s[:rem]
        res+="-"

    i = rem
    while i< len(s):
        res += s[i:i + k]
        if i+k<len(s):
            res += "-"
        i += k

    return res.upper()
s = "5F3Z-2e-9-w"
k = 4
print(licenseKeyFormatting(s,k))