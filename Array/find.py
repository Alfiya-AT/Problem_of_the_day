# First and Last in Sorted
class Solution:
    def find_x(self, arr, x):
        # code here
        first=-1
        last=-1
        left=0
        right=len(arr)-1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == x:
                first = mid
                right = mid - 1   # keep searching on left side

            elif arr[mid] < x:
                left = mid + 1

            else:
                right = mid - 1

        # Find last occurrence
        left = 0
        right = len(arr) - 1







        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == x:
                last = mid
                left = mid + 1    # keep searching on right side

            elif arr[mid] < x:
                left = mid + 1

            else:
                right = mid - 1

        return [first, last]

arr= [1, 3, 5, 5, 5, 5, 67, 123, 125] 
x = 5
s=Solution()
print(s.find_x(arr,x))