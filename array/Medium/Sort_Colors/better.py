from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        zeros = 0
        ones = 0
        twos = 0
        for i in range(0, n):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
            else:
                twos += 1
        print(zeros, ones, twos)
        for i in range(0, n):
            if i < zeros:
                nums[i] = 0
            elif i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2


nums = [2, 0, 2, 1, 1, 0]
obj = Solution()
obj.sortColors(nums)
print(nums)
