from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def BSL(nums: List[int], target: int):
            n = len(nums)
            ans = -1
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    ans = mid
                    high = mid - 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        def BSR(nums: List[int], target: int):
            n = len(nums)
            ans = -1
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    ans = mid
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        if not nums:
            return [-1, -1]
        left = BSL(nums, target)
        if left == -1:
            return [-1, -1]
        right = BSR(nums, target)
        return [left, right]