from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        i = 0
        j = i + 1
        while j < n:
            if nums[j] > nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        return i + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
obj = Solution()
print(obj.removeDuplicates(nums))