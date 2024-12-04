from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for i in range(0, n + 1):
            d[i] = 0

        for i in range(0, n):
            d[nums[i]] = 1

        for k, v in d.items():
            if v == 0:
                return k


nums = [3, 0, 1]
obj = Solution()
print(obj.missingNumber(nums))
