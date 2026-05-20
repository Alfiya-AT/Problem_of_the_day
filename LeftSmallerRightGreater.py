# Left Smaller Right Greater
def LSRG(arr):
    for i in range(len(arr)):
        left=0
        right=len(arr)-1
        while left<arr[i] or right>arr[i]:
            if left<arr[i]:
                left+=1
            if right>arr[i]:
                right-=1
            else:
                break
        if i==right and i==left:
            
        # return -1

# arr = [4, 2, 5, 7]
# Output: 5
# print(LSRG(arr))