class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        for i in range(n - 2, -1, -1):
            swap = False
            for j in range(0, i + 1):
                if arr[j] > arr[j + 1]:
                    swap = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if swap == False:
                return arr
        return arr


arr = [3, 5, 9, 6, 7, 1, 8, 2]
obj = Solution()
print(obj.bubbleSort(arr, len(arr)))
