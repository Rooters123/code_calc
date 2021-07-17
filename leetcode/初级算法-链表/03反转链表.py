# encoding = utf-8
class Solution:
    def reverseList(self, head):
        pre = None
        cursor = head
        while cursor != None:
            # 将后节点暂存
            teamp = cursor.next
            # 将当前节点指向前一节点
            cursor.next = pre
            # 前一节点后移
            pre = cursor
            # 当前节点后移
            cursor = teamp
        return pre
