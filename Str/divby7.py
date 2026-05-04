class Solution:
    def isDivisibleBy7(self, s):
        remainder = 0

        for ch in s:
            digit = ord(ch) - ord('0')   # faster than int()
            remainder = (remainder * 10 + digit) % 7

        return 1 if remainder == 0 else 0

s="49"
obj=Solution()
print(obj.isDivisibleBy7(s))