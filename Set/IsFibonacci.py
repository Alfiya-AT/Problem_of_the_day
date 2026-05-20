class Solution():
    def solve(self, N, K, GeekNum):
        
        # Step 1: if N already within given list
        if N <= K:
            return GeekNum[N-1]
        
        # Step 2: initial window sum
        window_sum = sum(GeekNum)
        
        # Step 3: build sequence
        for i in range(K, N):
            next_val = window_sum
            GeekNum.append(next_val)
            
            # update window
            window_sum += next_val
            window_sum -= GeekNum[i-K]
        
        return GeekNum[-1]


# Test
obj = Solution()
print(obj.solve(5, 3, [0, 1, 2]))   # Output: 6