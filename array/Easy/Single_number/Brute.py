from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                return nums[i]


nums = [4, 2, 1, 2, 1]
obj = Solution()
print(obj.singleNumber(nums))
