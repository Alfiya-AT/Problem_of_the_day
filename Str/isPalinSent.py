class Solution:
    def isPalinSent(self, s):

        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        left = 0
        right = len(cleaned) - 1

        while left <= right:

            if cleaned[left] != cleaned[right]:
                return False

            left += 1
            right -= 1

        return True


obj = Solution()

print(obj.isPalinSent("Too hot to hoot"))
print(obj.isPalinSent("Abc 012..## 10cbA"))