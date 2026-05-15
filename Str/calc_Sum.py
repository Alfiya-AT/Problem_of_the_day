#User function Template for python3

class Solution:
    def calc_Sum(self, arr1, arr2):

        carry = 0
        res = []

        i = len(arr1)-1
        j = len(arr2)-1

        while i >= 0 or j >= 0 or carry:

            val = carry

            if i >= 0:
                val += arr1[i]
                i -= 1

            if j >= 0:
                val += arr2[j]
                j -= 1

            res.append(val % 10)
            carry = val // 10

        res.reverse()

        return "".join(str(x) for x in res)
arr1 = [1, 2]
arr2 = [2, 1]
obj=Solution()
print(obj.calc_Sum(arr1, arr2))