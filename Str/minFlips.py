class Solution:
    def minFlips(self, s):
        # Code here
        even=0
        odd=0
        for i in range(len(s)):
            expected_even='0' if i%2==0 else '1'
            if s[i]!=expected_even:
                even+=1

            expected_odd='1' if i%2==0 else '0'
            if s[i]!=expected_odd:
                odd+=1
        
        return min(even,odd)
        
res=Solution()
print(res.minFlips(s="0001010111"))