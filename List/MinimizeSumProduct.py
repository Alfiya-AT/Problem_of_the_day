#User function Template for python3

class Solution:
    def minValue(arr1, arr2):
        #code here
        arr1.sort()
        arr2.sort()
        n=len(arr2)-1
        res=0
        for i in range(len(arr1)):
            res+=arr1[i]*arr2[n-i]
        return res
        
c=Solution
print(c.minValue(arr1 = [3, 1, 1] , arr2 = [6, 5, 4]))
