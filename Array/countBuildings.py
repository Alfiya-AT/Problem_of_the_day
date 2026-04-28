#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        
        cnt=1
        max_height=height[0]
        for i in range(len(height)):
            if height[i]>max_height:
                max_height=height[i]
                cnt+=1
        return cnt
        
height = [7,7, 8,3, 2, 9,7]
res=Solution()
print(res.countBuildings(height))