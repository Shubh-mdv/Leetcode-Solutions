class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        max_len = 0
        for i in range(0, n):
            for j in range(i, n):
                s = 0
                for l in range(i, j + 1):
                    s += arr[l]
                if s == k:
                    max_len = max(max_len, j - i + 1)
        return max(max_len, j - i + 1)


arr = [10, 5, 2, 7, 1, 9]
obj = Solution()
print(obj.lenOfLongSubarr(arr, len(arr), 15))
