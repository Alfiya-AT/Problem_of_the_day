class Solution:
    def repeatingCharacter(self,s):
        #code here
        for i in range(len(s)):
            if s[i] in s[i+1:]:
                return i
        return -1
s = "geeksforgeeks"
obj=Solution()
print(obj.repeatingCharacter(s))