from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
