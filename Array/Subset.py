class Solution:

    def subsets(self, arr):

        res = []

        def solve(index, path):

            # base case
            if index == len(arr):
                res.append(path[:])
                return

            # include current element
            path.append(arr[index])
            solve(index + 1, path)

            # backtrack
            path.pop()

            # exclude current element
            solve(index + 1, path)

        solve(0, [])

        return res


obj = Solution()

arr = [1, 2, 3]

print(obj.subsets(arr))