from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        original_total = (n * (n + 1)) // 2
        return original_total - sum(nums)


nums = [3, 0, 1]
obj = Solution()
print(obj.missingNumber(nums))
