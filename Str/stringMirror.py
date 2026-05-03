class Solution:
    def stringMirror(self, str : str) -> str:
        # code here

        val=str[0]
        
        for i in range(1,len(str)):
            if str[i]<str[i-1]:
                val+=str[i]
            else:
                break
        # res=str[:(str.index(m))+1]
        return val+val[::-1]


str = "casd"
obj=Solution()
print(obj.stringMirror(str))
