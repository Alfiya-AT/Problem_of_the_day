#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        res=[]
        b.sort()
        for i in a:
            count=0
            j=0
            while j<n and i>=b[j]:
                count+=1
                j+=1

            res.append(count)
        return res
        

obj=Solution()
n = 4
a = [1,1,5,5]
b = [0,1,2,3]
q = 4
query = [0,1,2,3]

print(obj.countElements(a,b,n,query,q))