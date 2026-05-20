def SumOfSubSeq(s="128"):
# try to understnd the ans some times it not sloved the way on which it is asked go through the ans 
# for ex:
# Input:  S = "123" 
# Output: 24
# Explanation: {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 3}, {1, 2, 3} are all possible sub-sequences
#  1,2,3-> 4   all have came 4 time 
# it means the res = (sum of dig )*2^n-1    
    sumdig=0
    for i in s:
        sumdig+=int(i)
    return ((sumdig)*2**(len(s)-1))

print(SumOfSubSeq())