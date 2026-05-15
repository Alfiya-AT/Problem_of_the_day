class Solution:
    def countSubstring(self, s):
        # code here
        l=len(s)
        left=0
        count=0
        while left<l:
            if s[left] in s[left+1:]:
                count+=1
            left+=1
        return count+len(s)

s="aba"
obj=Solution()
print(obj.countSubstring(s))