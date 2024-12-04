from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_lst = []
        n = len(nums)
        for i in range(0, n):
            if nums[i] != 0:
                non_zero_lst.append(nums[i])

        nzl = len(non_zero_lst)
        for i in range(0, nzl):
            nums[i] = non_zero_lst[i]

        for i in range(nzl, n):
            nums[i] = 0


nums = [0, 1, 0, 3, 12]
obj = Solution()
obj.moveZeroes(nums)
print(nums)
