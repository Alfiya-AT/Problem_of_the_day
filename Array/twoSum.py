class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in d :
                return [d[complement],i]
            d[nums[i]]=i
        return [-1,-1]
obj=Solution()
print(obj.twoSum([3,4,2,3,7,11,15],9))