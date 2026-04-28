class Solution:
    # Function to add one to a number represented as an array
    def addOne(self,arr):
        # code here
        # num="".join(arr)
        # num=int(num)
        # num+=1
        # num=str(num)
        # return list(num)
        
        carry=1
        res=[]
        for i in range(len(arr)-1,-1,-1):
            val=arr[i]+carry
            
            res.append(val%10)
            carry=val//10
            
        if carry==1:
            res.append(1)

        return res[::-1]

# arr = ["5", "6", "7", "8"]
arr = [9, 9, 9, 9]
res=Solution()
print(res.addOne(arr))