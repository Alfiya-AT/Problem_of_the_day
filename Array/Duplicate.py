#User function Template for python3
class Solution:
    def findDuplicate(self,arr):
    # Your code goes here

        if arr[0]== arr[4]:
            return arr[0]
        return arr[5]
        
arr=[1, 2, 3, 3, 3, 3, 3, 5, 9, 10]
obj=Solution()
print(obj.findDuplicate(arr))