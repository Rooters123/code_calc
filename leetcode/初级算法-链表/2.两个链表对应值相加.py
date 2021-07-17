# encoding = utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        h = self
        l = []
        while h:
            l.append(str(h.val))
            h = h.next
        return ','.join(l)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        new_list = dummy
        chg = 0
        mid_val = 0
        while l1 or l2:
            if l1 and l2:
                if l1.val + l2.val + chg >= 10:
                    mid_val =  l1.val + l2.val + chg
                    new_list.next = ListNode(mid_val - 10)
                    new_list = new_list.next
                    chg = 1
                else:
                    mid_val =l1.val + l2.val + chg
                    new_list.next = ListNode(mid_val)
                    new_list = new_list.next
                    chg = 0
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if l1.val + chg >=10:
                    mid_val = l1.val + chg
                    new_list.next = ListNode(mid_val - 10)
                    new_list = new_list.next
                    chg = 1
                else:
                    mid_val = l1.val  + chg
                    new_list.next = ListNode(mid_val)
                    new_list = new_list.next
                    chg = 0
                l1 = l1.next
            else:
                if l2.val + chg >=10:
                    mid_val = l2.val + chg
                    new_list.next = ListNode(mid_val - 10)
                    new_list = new_list.next
                    chg = 1
                else:
                    mid_val = l2.val  + chg
                    new_list.next = ListNode(mid_val)
                    new_list = new_list.next
                    chg = 0
                l2 = l2.next
        if mid_val >= 10:
            new_list.next = ListNode(1)
        return dummy.next

    def l2chiain(self,l):
        dummy = ListNode()
        h = dummy
        for num in l:
            h.next = ListNode(num)
            h = h.next
        return dummy.next


s = Solution()
head = s.l2chiain([9,9,9,9,9,9,9])
head2 = s.l2chiain([9,9,9,9])
print(s.addTwoNumbers(head,head2))