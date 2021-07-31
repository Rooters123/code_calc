# -*- coding: UTF-8 -*-
"""
@author:zhubangren
@file:二叉树-练习.py
@time:2021/07/31
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            val_list.append(node.val)
            dfs(node.left)
            dfs(node.right)
        val_list = []
        dfs(root)
        return val_list



tree_list = []

s = Solution()
# s.preorderTraversal()

def bfs(root):
    if not root:
        return []
    res = []
    cur_lay = [root]
    while cur_lay:
        next_lay = []
        cur_lay_val = []
        for node in cur_lay:
            cur_lay_val.append(node.val)
            if node.left:
                next_lay.append(node.left)
            if node.right:
                next_lay.append(node.right)
        cur_lay = next_lay
        res.append(cur_lay_val)
    return res



