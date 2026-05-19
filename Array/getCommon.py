class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        set1=set(nums1)
        set2=set(nums2)
        return list(set1&set2)[0]
        
obj=Solution()
print(obj.getCommon([1,2,3,6],[2,3,4,5]))