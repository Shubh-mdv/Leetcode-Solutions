class Solution:
    def findUnion(self, arr1, arr2, n, m):
        merged = []
        i = 0
        j = 0
        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                if len(merged) == 0 or merged[-1] != arr1[i]:
                    merged.append(arr1[i])
                i += 1
            else:
                if len(merged) == 0 or merged[-1] != arr2[j]:
                    merged.append(arr2[j])
                j += 1

        while i < n:
            if len(merged) == 0 or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1

        while j < m:
            if len(merged) == 0 or merged[-1] != arr2[j]:
                merged.append(arr2[j])
            j += 1

        return merged


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]
obj = Solution()
print(obj.findUnion(arr1, arr2, len(arr1), len(arr2)))
