from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        L = 0
        R = n - 1
        while L < R:
            if nums[L] + nums[R] == target:
                return [L, R]
            elif nums[L] + nums[R] > target:
                R -= 1
            else:
                L += 1


# nums = [2, 7, 11, 15]
nums = [3, 2, 4]
obj = Solution()
print(obj.twoSum(nums, 6))
