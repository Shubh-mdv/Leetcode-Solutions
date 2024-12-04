# not contains duplicates
class Solution:
    def print2largest(self, arr):
        maxi = float("-inf")
        sec_maxi = float("-inf")
        n = len(arr)
        for i in range(0, n):
            if arr[i] > maxi:
                sec_maxi = maxi
                maxi = arr[i]

            elif arr[i] > sec_maxi and arr[i] != maxi:
                sec_maxi = arr[i]

        return sec_maxi


arr = [12, 35, 1, 10, 34, 1]
obj = Solution()
print(obj.print2largest(arr))
