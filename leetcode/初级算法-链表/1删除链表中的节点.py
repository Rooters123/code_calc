# encoding = utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        head = [4, 5, 1, 9]
        # 类似于将0移动到最后，最后进行截取
        j = 0
        for i in range(len(head)):
            if head[i] != node:
                head[i],head[j] = head[j],head[i]
                j += 1
        head[:] = head[0:(len(head) - 1)]
        print(head)

        # node.val = node.next.val
        # node.next = node.next.next
        pass




s = Solution()
s.deleteNode(5)
