#User function Template for python3
class Solution:
    def search(self, text, pat):
        
        return 1 if pat in text else 0

text = "geeksforgeeks"
pat = "geek"
obj=Solution()
print(obj.search(text,pat))