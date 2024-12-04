from typing import List


# Rotate array by one place
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> List:
#         n = len(nums)
#         nums[:] = [nums[-1]] + nums[0 : n - 1]

#         return nums


# nums = [1, 2, 3, 4, 5, 6, 7]
# obj = Solution()
# print(obj.rotate(nums, 1))


# Rotate array by K steps
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> List:
#         n = len(nums)
#         nums[:] = nums[n - k : n] + nums[0 : n - k]

#         return nums


# nums = [1, 2, 3, 4, 5, 6, 7]
# obj = Solution()
# print(obj.rotate(nums, 3))
