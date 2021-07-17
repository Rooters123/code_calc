# encoding = utf-8
class Solution:
    def findKthLargest(self, nums, k):
        def quickSort(start,end):
            if start >= end:
                return nums[end]
            low = start
            high = end
            base_data = nums[low]
            while low < high:
                while low < high and nums[high] < base_data:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] >= base_data:
                    low += 1
                nums[high] = nums[low]

            nums[low] = base_data
            print(nums,low)
            if low == k - 1:
                return nums[low]
            elif low < k - 1:
                return quickSort(low+1,end)
            else:
                return quickSort(start,low-1)
        return quickSort(0,len(nums)-1)

# class Solution:
#     def findKthLargest(self, nums, k):
#
#         def partition(array, left,right):
#             i = left-1
#             for j in range(left,right):
#                 if array[j]<=array[right]:
#                     i += 1
#                     array[i], array[j] = array[j],array[i]
#             array[i+1], array[right] = array[right],array[i+1]
#             print(array,i)
#             return i+1
#
#         def quickSort(array,left,right,k):
#             if left<=right:
#                 pivot = partition(array,left,right)
#                 if pivot == len(array) - k:
#                     return array[pivot]
#                 elif pivot < len(array) - k:
#                     return quickSort(array,pivot+1,right,k)
#                 else:
#                     return quickSort(array,left,pivot-1,k)
#
#         return quickSort(nums,0,len(nums)-1,k)
s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6] ,9))