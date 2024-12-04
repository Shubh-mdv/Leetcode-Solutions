from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()


nums = [2, 0, 2, 1, 1, 0]
obj = Solution()
obj.sortColors(nums)
print(nums)
