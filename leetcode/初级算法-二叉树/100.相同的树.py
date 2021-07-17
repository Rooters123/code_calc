# encoding = utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def __init__(self):
#         self.left_p = []
#         self.left_q = []
#         self.mid_p = []
#         self.mid_q = []
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         # 一开始的想法是通过遍历两个数的前序和中序，最后来确定这两个数组是否一致
#         self.leftFind(p,self.left_p)
#         self.leftFind(q,self.left_q)
#         self.midFind(p,self.mid_p)
#         self.midFind(q,self.mid_q)
#         print(self.left_p,self.left_q)
#         print(self.mid_p,self.mid_q)
#         if self.left_p == self.left_q and self.mid_p == self.mid_q:
#             return True
#         return False
#
#     def leftFind(self,cur:TreeNode,ret):
#         if not cur:
#             # 注意这里是需要添加为None的，因为不添加的话，树[1,1]和树[1,null,1]的结果是一样的
#             ret.append(None)
#             return
#         ret.append(cur.val)
#         self.leftFind(cur.left,ret)
#         self.leftFind(cur.right,ret)
#     def midFind(self,cur:TreeNode,ret):
#         if not cur:
#             ret.append(None)
#             return
#         self.midFind(cur.left,ret)
#         ret.append(cur.val)
#         self.midFind(cur.right,ret)
#


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 判断是够两个分支都为空
        if not p and not q:
            return True
        # 其中有一个为空则返回False
        elif not p or not q :
            return False
        elif p.val!= q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)