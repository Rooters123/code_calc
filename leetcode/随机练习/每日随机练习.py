# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # dfs
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left,right) + 1
    # bfs
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret = [root]
        alist = []
        count = 1
        while ret:
            alist = alist.append([i.val for i in ret])
            new_code = []
            for i in ret:
                if i.left:
                    new_code.append(i.left)
                if i.right:
                    new_code.append(i.right)
            ret = new_code
            count += 1
        return count

if __name__ == '__main__':

    def maxVal(alist):
        if  len(alist) == 1:
            return alist[0]
        sum = 0
        for i in range(len(alist)):
            maxval = max(0, interval)
            interval = sum + alist[i]

