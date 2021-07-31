# encoding = utf-8
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
#     一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.flag = 0
    def isBalanced(self, root: TreeNode) -> bool:
        # 从底向上，判断左右子树的高度
        if not root:
            return True
        self.balanceLever(root)
        if self.flag == -1:
            return False
        else:
            return True
    def balanceLever(self,root):
        if not root:
            return 0
        left = self.balanceLever(root.left)
        right = self.balanceLever(root.right)
        if abs(left - right) > 1:
            self.flag = -1
        # 注意这里的的return语句外面是不需要包含else的
        return max(left,right) + 1

    # def isBalanced(self, root: TreeNode) -> bool:
    #     def deep(root):
    #         if not root:
    #             return 0
    #         leftnum = self.isBalanced(root.left)
    #         rightnum = self.isBalanced(root.right)
    #         if leftnum == -1 or rightnum == -1 or abs(leftnum - rightnum) > 1:
    #             return - 1
    #         else:
    #             return max(leftnum, rightnum) + 1
    #
    #     num = deep(root)
    #     return num >= 0