class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        res = []
        for i in range(0, n):
            for j in range(i + 1, n):
                if arr[j] > arr[i] and arr[j] not in res:
                    res.append(arr[j])
                    break
            if i == n - 1:
                res.append(arr[i])
        return res


arr = [16, 17, 4, 3, 5, 2]
obj = Solution()
print(obj.leaders(len(arr), arr))
