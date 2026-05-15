class Solution:
    def isSubSeq(self, s1, s2):

        i = 0   # pointer for s1
        j = 0   # pointer for s2

        while i < len(s1) and j < len(s2):

            # if characters match
            if s1[i] == s2[j]:
                i += 1

            # always move j
            j += 1

        # if all chars of s1 matched
        return i == len(s1)


s1 = "AXY"
s2 = "YADXCP"

obj = Solution()
print(obj.isSubSeq(s1, s2))