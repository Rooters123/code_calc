# encoding = utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        ret = head = ListNode()
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    ret.next = l1
                    l1 = l1.next
                    ret = ret.next
                else:
                    ret.next = l2
                    l2 = l2.next
                    ret = ret.next

            elif l1:
                ret.next = l1
                ret = ret.next
                l1 = l1.next
            else:
                ret.next = l2
                ret = ret.next
                l2 = l2.next
        return head.next

