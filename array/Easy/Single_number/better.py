from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in range(0, n):
            d[nums[i]] = d.get(nums[i], 0) + 1

        for k, v in d.items():
            if v == 1:
                return k


nums = [4, 2, 1, 2, 1]
obj = Solution()
print(obj.singleNumber(nums))
