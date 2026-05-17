class Solution:

    def maxZero(self, arr):
        res = max(arr, key = lambda num: (num.count("0"), len(num), int(num)))    
        return res if res.count("0") != 0 else -1
        # mx = 0
        # ans = -1

        # for num in arr:

        #     temp = num
        #     cnt = 0

        #     while temp > 0:

        #         if temp % 10 == 0:
        #             cnt += 1

        #         temp //= 10

        #     if cnt > mx:
        #         mx = cnt
        #         ans = num

        #     elif cnt == mx and cnt > 0:
        #         ans = max(ans, num)

        # return ans


obj = Solution()

arr = [10, 20, 3000, 9999, 200]

print(obj.maxZero(arr))