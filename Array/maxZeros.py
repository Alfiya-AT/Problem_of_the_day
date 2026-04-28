class Solution:
    def maxZeros(self, arr):
        # code here
        val=-1
        mx=0
        for i in range(len(arr[0])):
            cnt=0
            for j in range(len(arr)):
                if arr[j][i]==0:
                    cnt+=1
            print("cnt",cnt)
            if cnt>mx:
                mx=cnt
                print("mx",mx)
                val=i
                print("val",val)

        
        return val


arr = [[1, 0, 1],[0, 0, 0],[0, 1, 0]]
# row 0 → 2
# row 1 →2
# row 2 → 2
# arr = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
# arr=[[1, 1, 1, 0, 0 ,0, 1, 1],[0, 1, 0 ,0, 0, 0, 1, 1],[1, 1 ,0 ,0 ,1, 1, 0, 0]]
res=Solution()
print(res.maxZeros(arr))