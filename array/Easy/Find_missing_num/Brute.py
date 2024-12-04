from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n):
            if i not in nums:
                return i


nums = [3, 0, 1]
obj = Solution()
print(obj.missingNumber(nums))
