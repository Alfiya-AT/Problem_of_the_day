def smallest(arr):
    f=float('inf')
    s=float('inf')
    for x in arr:
        if x<f and f>s:
            s=f
            f=x
    if f==s:
        return [-1]
    return [f,s]


# or 

class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        sorted_arr=sorted(list(set(arr)))
        if len(sorted_arr)>1:
            return sorted_arr[0],sorted_arr[1]
        else:
            return [-1]

# arr=[ 4, 3, 5, 6,2]
# arr=[1,1,1]
arr=[2, 3, 4]
# Output: [2, 3]
print(smallest(arr))
