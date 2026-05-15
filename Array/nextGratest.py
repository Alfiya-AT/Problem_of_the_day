class Solution:
    def nextGreatest(self,arr):
        max_so_far=-1
        for i in range(len(arr)-1,-1,-1):
            temp=arr[i]
            arr[i]=max_so_far
            max_so_far=max(temp,max_so_far)





        return arr

obj=Solution()
arr=[16, 17, 4, 3, 5, 2]
# [17, 5, 5, 5, 2, -1]
print(obj.nextGreatest(arr))