from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for i in range(0, n):
            d[nums[i]] = 0

        j = 0
        for key in d:
            nums[j] = key
            j += 1

        return j


nums = [1, 1, 2]
obj = Solution()
print(obj.removeDuplicates(nums))
