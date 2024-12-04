from typing import List


# Rotate array by one place
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> List:
#         element = nums.pop()
#         nums.insert(0, element)

#         return nums


# nums = [1, 2, 3, 4, 5, 6, 7]
# obj = Solution()
# print(obj.rotate(nums, 1))


# Rotate array by K steps
class Solution:
    def rotate(self, nums: List[int], k: int) -> List:
        for _ in range(k):
            element = nums.pop()
            nums.insert(0, element)

        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
obj = Solution()
print(obj.rotate(nums, 3))
