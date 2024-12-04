# optimal for +ve and -ve
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        sum = 0
        sum_map = {}
        max_len = 0
        for i in range(0, n):
            sum += arr[i]
            if sum == k:
                max_len = i + 1
            rem = sum - k
            if rem in sum_map:
                l = i - sum_map[rem]
                max_len = max(max_len, l)
            if sum not in sum_map:
                sum_map[sum] = i
        return max_len


arr = [10, 5, 2, 7, 1, 9]
obj = Solution()
print(obj.lenOfLongSubarr(arr, len(arr), 15))
