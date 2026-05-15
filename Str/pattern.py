class Solution:
    def pattern(self, n):
        # code here
        res=[]
        
        while n>0:
            
            res.append(n)
            n-=5
        if n<=0:
            res.append(n)
            rev=res[::-1]
            r=res+rev[1:]
        return  r
            
        

n=10
obj=Solution()
print(obj.pattern(n))