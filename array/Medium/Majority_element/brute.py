from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(0, n):
            for j in range(i, n):
                if nums[i] == nums[j]:
                    count += 1
            if count > n // 2:
                return nums[i]


nums = [2, 2, 1, 1, 1, 2, 2]
obj = Solution()
print(obj.majorityElement(nums))
