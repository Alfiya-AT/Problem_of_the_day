class Solution:
    def countDigitK(self, k, arr):
        # code here
        count=0
        for i in arr:
            while i>0:
                if i%10==k:
                    count+=1
                i//=10

        return count

k = 1
arr = [11, 12, 13, 14, 15]
s = Solution()
print(s.countDigitK(k, arr))