class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num<=9:
            return num
        sum=num
        while sum>9:
            val=(sum%10)
            sum=sum//10
            if num==0:
                num=sum
                sum=0 
        return num
    
obj=Solution()
print(obj.addDigits(38))