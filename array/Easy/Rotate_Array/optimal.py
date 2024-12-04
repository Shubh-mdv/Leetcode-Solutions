from typing import List


# Rotate array by one place
class Solution:
    def reverse(self, nums: List[int], l: int, r: int):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> List:
        n = len(nums)
        k = k % n
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, 0, n - 1)

        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
obj = Solution()
print(obj.rotate(nums, 3))
