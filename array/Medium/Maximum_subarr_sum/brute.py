from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        for i in range(0, n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                maxi = max(maxi, total)
        return maxi


nums = [5, 4, -1, 7, 8]  # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Solution()
print(obj.maxSubArray(nums))
