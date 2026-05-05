#User function Template for python3

class Solution:

    def transform(self, S):
        # code here
        res=[]
        count=1
        lower_case=S.lower()
        for i in range(1,len(lower_case)):
            if lower_case[i]!=lower_case[i-1]:
                res.append(str(count))
                res.append(lower_case[i-1])
                count=1
            else:
                count+=1
        res.append(str(count))
        res.append(lower_case[-1])
        return ''.join(res)





        # res=""
        # count=1
        # lower_case=S.lower()
        # for i in range(1,len(lower_case)):
        #     if lower_case[i]!=lower_case[i-1]:
        #         res+=(str(count))+(lower_case[i-1])
        #         count=1
        #     else:
        #         count+=1
        # res+=(str(count))+(lower_case[-1])
        # return res

obj=Solution()
print(obj.transform("aaABBbc"))