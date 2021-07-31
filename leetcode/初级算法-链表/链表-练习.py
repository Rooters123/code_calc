# -*- coding: UTF-8 -*-
"""
@author:zhubangren
@file:链表-练习.py
@time:2021/07/31
"""
class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        pre = None
        cursor = head
        while cursor:
            temp_var = cursor.next
            cursor.next = pre
            pre = cursor
            cursor = temp_var
        return pre
