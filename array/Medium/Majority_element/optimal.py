from typing import List


# Moore's voting Algorithm
# Below solution is for when problem statement mentioned that majority element always exist
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         candidate = nums[0]
#         count = 1
#         for i in range(1, n):
#             if nums[i] == candidate:
#                 count += 1
#             else:
#                 count -= 1
#             if count == 0:
#                 candidate = nums[i]
#                 count = 1
#         return candidate


# nums = [2, 2, 1, 1, 1, 2, 2]
# obj = Solution()
# print(obj.majorityElement(nums))


# May or may not exist
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        candidate = nums[0]
        count = 1
        cand_counter = 0
        for i in range(1, n):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1
        for i in range(0, n):
            if nums[i] == candidate:
                cand_counter += 1
        if cand_counter > n // 2:
            return candidate
        return False


nums = [2, 2, 1, 1, 1, 2]
obj = Solution()
print(obj.majorityElement(nums))
