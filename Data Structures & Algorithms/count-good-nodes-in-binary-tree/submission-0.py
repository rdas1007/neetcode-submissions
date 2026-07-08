# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        currMax = root.val
        count = 0
        def isgood(root, currMax):
            nonlocal count
            if root.val >= currMax:
                count += 1
            currMax = max(currMax, root.val)
            if root.left:
                isgood(root.left, currMax)
            if root.right:
                isgood(root.right, currMax)
        isgood(root, currMax)
        return count

