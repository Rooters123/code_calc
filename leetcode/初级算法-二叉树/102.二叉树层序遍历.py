# encoding = utf-8
# Definition for a binary tree node.
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/python3-er-cha-shu-ceng-xu-bian-li-by-jo-nlx3/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        #跟结点入queue
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            #存储当前层的孩子节点列表
            ll = []
            #对当前层的每个节点遍历
            for node in queue:
                #如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                #如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            #后把queue更新成下一层的结点，继续遍历下一层
            queue = ll
        return res

    def levelOrder2(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        # 将根节点放到数组中
        nodelist= [root]
        res = []
        while nodelist:
            res.append([i.val for i in nodelist])
            new_node = []
            for i in nodelist:
                if i.left:
                    new_node.append(i.left)
                if i.right:
                    new_node.append(i.right)
            nodelist = new_node
        return res

