#User function Template for python3

def find4Numbers( A, n, X):
    # return true or false
    A.sort()
    for item1 in range(len(A)-3): 
        for item2 in range(item1+1, len(A)-2):
            left = item2+1
            right = len(A)-1
            target = X - (A[item1]+A[item2])
            while left < right:
                curr_sum = A[left] + A[right]
                if curr_sum == target:
                    return True
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return False

n = 6
A = [1, 5, 1, 0, 6, 0]
X = 7
print(find4Numbers( A, n, X))