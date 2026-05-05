#User function Template for python3

class Solution:
    def BalancedString(self,N):
        #code here
        val="abcdefghijklmnopqrstuvwxyz"
        res=""
        while N>26:
            res+=val
            N-=26
        
        if N%2==0:
            start=N//2
            end=N//2
        else:
            digit_sum=sum(int(d) for d in str(N))
            if digit_sum%2==0:
                start=(N+1)//2
                end=(N-1)//2
            else:
                start=(N-1)//2
                end=(N+1)//2

        string=val[:start]+val[(26-end):]
        return string
N=21
obj=Solution()
print(obj.BalancedString(N))