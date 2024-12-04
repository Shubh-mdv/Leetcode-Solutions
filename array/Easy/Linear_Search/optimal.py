class Solution:
    def searchInSorted(self, arr, N, K):
        for i in range(0, N):
            if arr[i] == K:
                return 1
        return -1


arr = [1, 2, 3, 4, 6]
obj = Solution()
print(obj.searchInSorted(arr, len(arr), 6))
