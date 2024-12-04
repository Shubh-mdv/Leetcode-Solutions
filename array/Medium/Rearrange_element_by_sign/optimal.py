from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        p = 0
        n = 0
        for i in range(0, n):
            if nums[i] > 0:
                res[p] = nums[i]
                p += 2
            else:
                res[n] = nums[i]
                n += 1
        return res


nums = [3, 1, -2, -5, 2, -4]
obj = Solution()
print(obj.rearrangeArray(nums))
