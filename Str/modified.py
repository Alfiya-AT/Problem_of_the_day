class Solution:
    def modified(self, s):
        #code here

        cnt=1
        res=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cnt+=1
            else:
                cnt=1

            if cnt==3:
                res+=1
                cnt=1

        return res



        # start=0
        # end=1
        # cnt=1
        # res=0
        # while end<len(s):
            
        #     if s[start]!=s[end]:
        #         start=end
        #         cnt=1
        #     elif s[start]==s[end]:
        #         cnt+=1
        #     if cnt==3:
        #         res+=1
        #         start=end
        #         cnt=1
            
        #     end+=1
            
        # return res

s="aaaabaaabaa"
obj=Solution()
print(obj.modified(s))