from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [2, 7, 11, 15]
# nums = [3, 2, 4]
obj = Solution()
print(obj.twoSum(nums, 6))
