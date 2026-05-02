#User function Template for python3

from multiprocessing.sharedctypes import Value


class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d={}       
        for name in arr:
            d[name]=d.get(name,0)+1

        max_votes=0
        winner_name=""

        for name,count in d.items():
            if count>max_votes:
                max_votes=count
                winner_name=name
            elif count==max_votes:
                if winner_name=="" or name<winner_name:
                    winner_name=name
        return [winner_name,str(max_votes)]


        
n = 13
arr= ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
res=Solution()
print(res.winner(arr,n))