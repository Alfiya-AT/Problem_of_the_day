class Solution:
    def printString(self, s, ch, count):
	    # code here
        for i in range(len(s)):
            if s[i]==ch:
                count-=1
            if count==0:
                return s[i+1:]

        return ""

# Input: 
s = "Thisisdemostring"
ch = 'i'
count = 3
# Output: ng
res=Solution()
print(res.printString(s,ch,count))