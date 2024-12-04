# not contains duplicates
class Solution:
    def print2largest(self, arr):
        n = len(arr)
        arr.sort()

        return arr[n - 2]


arr = [12, 35, 1, 10, 34, 1]
obj = Solution()
print(obj.print2largest(arr))
