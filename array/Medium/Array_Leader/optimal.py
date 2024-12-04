class Solution:
    # Back-end complete function Template for Python 3
    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        res = []
        maxi = float("-inf")
        for i in range(n - 1, -1, -1):
            if arr[i] > maxi:
                maxi = arr[i]
                res.append(maxi)
        res.reverse()
        return res


arr = [16, 17, 4, 3, 5, 2]
obj = Solution()
print(obj.leaders(len(arr), arr))
