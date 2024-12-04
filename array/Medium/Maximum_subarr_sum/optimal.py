from typing import List


# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        sum = 0
        for i in range(0, n):
            sum += nums[i]
            maxi = max(maxi, sum)
            if sum < 0:
                sum = 0
        return maxi


nums = [5, 4, -1, 7, 8]  # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Solution()
print(obj.maxSubArray(nums))
