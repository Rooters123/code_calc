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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        newhead = head
        while newhead.next:
            if newhead.next.val == newhead.val:
                # 如果最后两位数字是重复的话，也是符合的
                # 如果newhead.next为最后一位的话，newhead.next.next就是为None，自然而然的就将最后两位数字进行了去重
                newhead.next = newhead.next.next
            else:
                newhead = newhead.next
        return head
def l2chiain(l):
    dummy=ListNode()
    h=dummy
    for num in l:
        h.next = ListNode(num)
        h=h.next
    return dummy.next
head = l2chiain([1,1,2,2,2,2])
print(head.next)
s = Solution()
h = s.deleteDuplicates(head)
print(h)