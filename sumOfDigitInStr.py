def findSum( s = "geeks4geeks46"):
        #code here
        sumd=0
        left=0
        right=0
        while right<len(s):
            val=s[left:right+1]
            if val.isdigit():
                while right<len(s) and s[right].isdigit():
                    right+=1
                sumd+=int(s[left:right])
                # print(s[left:right])
                left=right
            else:
                left+=1
                right+=1
        
        return sumd

print(findSum())