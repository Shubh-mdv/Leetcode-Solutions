from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count = 0
        max_count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        return max(max_count, count)


nums = [1, 1, 0, 1, 1, 1]
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))
