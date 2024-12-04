# Input: arr = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
# Input: arr = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.
# Input: arr = [10]
# Output: 10
# Explanation: There is only one element which is the largest.
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

# Constraints:
# 1 <= arr.size()<= 106
# 0 <= arr[i] <= 106


from typing import List


class Solution:
    def largest(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()

        return arr[n - 1]


arr = [10]
obj = Solution()
print(obj.largest(arr))
