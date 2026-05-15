class Solution:
    def pairsum(self,arr):
        # code here
        arr.sort()
        result=arr[-1]+arr[-2]
        return result
    
arr=[11, 22, 33, 14, 50]
obj=Solution()
print(obj.pairsum(arr))