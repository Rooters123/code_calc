class Solution:
    def MySort(self, arr):
        # write code here

        def quicksort(alist, start, end):
            if start >= end:
                return alist
            low = start
            high = end
            base_data = alist[low]
            while low < high:
                while low < high and alist[high] > base_data:
                    high -= 1
                alist[low] = alist[high]
                while low < high and alist[low] <= base_data:
                    low += 1
                alist[high] = alist[low]
            alist[low] = base_data
            quicksort(alist, start, low - 1)
            quicksort(alist, low + 1, end)

        quicksort(arr, 0, len(arr) - 1)

        print(arr)


s = Solution()
s.MySort([54,26,93,17,77,17,31,44,55,20])

