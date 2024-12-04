# optimal for +ve only
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        sum = arr[0]
        max_len = 0
        L, R = 0, 0
        while R < n:
            while L <= R and sum > k:
                sum -= arr[L]
                L += 1
            if sum == k:
                max_len = max(max_len, R - L + 1)

            R += 1
            if R < n:
                sum += arr[R]

        return max_len


arr = [10, 5, 2, 7, 1, 9]
obj = Solution()
print(obj.lenOfLongSubarr(arr, len(arr), 15))
