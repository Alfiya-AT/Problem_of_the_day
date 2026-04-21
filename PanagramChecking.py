def checkPangram(s="dfdfw"):
        #code here
        res=""
        for i in s:
            if i.lower() not in res and i.isalpha():
                res+=i.lower()
        if len(res)==26:
            return True
        return False
print(checkPangram())