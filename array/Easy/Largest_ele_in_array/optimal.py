from typing import List


class Solution:
    def largest(self, arr: List[int]) -> int:
        maxi = 0
        for i in range(0, len(arr)):
            # if arr[i] > maxi:
            #     maxi = arr[i]
            maxi = max(maxi, arr[i])

        return maxi


arr = [1, 8, 7, 56, 90]
obj = Solution()
print(obj.largest(arr))


# Edge case
# If all the values are -ve in given array
class Solution:
    def largest(self, arr: List[int]) -> int:
        maxi = float("-inf")
        for i in range(0, len(arr)):
            # if arr[i] > maxi:
            #     maxi = arr[i]
            maxi = max(maxi, arr[i])

        return maxi


arr = [1, 8, 7, 56, 90]
obj = Solution()
print(obj.largest(arr))
