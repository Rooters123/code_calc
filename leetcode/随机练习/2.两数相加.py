# encoding = utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        cursor = ListNode()
        cursor.next = l1
        new_list = []
        while cursor.next:
            new_list.append(l1.val + l2.val)
            cursor = cursor.next
        print(new_list)

class SingleLink(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        # 链表是否为空
        return self._head == None
    def length(self):
        # 链表长度
        if self.is_empty():
            return 0
        cursor = self._head
        count = 1
        while cursor.next != None:
            count += 1
            cursor = cursor.next
        return count


    def travel(self):
        # 遍历整个链表
        cursor = self._head
        pre = None
        while cursor != None:
            print(cursor.val)
            pre = cursor
            cursor = cursor.next

    def prepend(self,item):
        # 链表头部添加元素
        nd = ListNode(item)
        nd.next = self._head
        self._head = nd

    def append(self,item):
        # 链表尾部添加元素
        nd = ListNode(item)
        if self.is_empty():
            self._head = nd
        else:
            cursor = self._head
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = nd

    def insert(self,pos, item):

        # 指定位置添加元素
        if pos <= 0:
            self.prepend(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            cursor = self._head
            nd = ListNode(item)
            while count + 1 < pos :
                cursor = cursor.next
                count += 1
            nd.next = cursor.next
            cursor.next = nd

    def remove(self,item):
        # 删除节点
        cursor = self._head
        pre = None
        while cursor != None:
            if cursor.val == item:
                if not pre:
                    self._head = None
                else:
                    pre.next = cursor.next
                break
            else:
                pre = cursor
                cursor = cursor.next

    def search(self,item):
        # 查找节点是否存在
        cursor = self._head
        count = 0
        while cursor:
            if item == cursor.item:
                return count
            else:
                cursor = cursor.next
        return -1

l1 = SingleLink()
l2 = SingleLink()
l1.append(ListNode(2))
l1.append(ListNode(4))
l1.append(ListNode(3))
l2.append(ListNode(5))
l2.append(ListNode(6))
l2.append(ListNode(4))
s =Solution()
s.addTwoNumbers(l1,l2)