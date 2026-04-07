def roundToNearest (s) : 
    res="0"
    i=-2
    carry=1
        
    if int(s[-1])>5:        
        while i>=-len(s) and carry!=0:
            val=int(s[i])+carry
            carry=val//10
            digit=val%10          
            res=str(digit)+res
            i-=1     
        if carry==1:
            res="1"+res
        else:
            res=s[:i+1]+res
    else:
        res=s[:-1]+res   
    return res


s = "29" 
print(roundToNearest(s))
# Output: 030