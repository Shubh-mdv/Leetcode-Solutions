from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}
        for i in range(0, n):
            rem = target - nums[i]
            if rem in hash_map:
                return [hash_map[rem], i]
            else:
                hash_map[nums[i]] = i


nums = [2, 7, 11, 15]
# nums = [3, 2, 4]
obj = Solution()
print(obj.twoSum(nums, 9))
