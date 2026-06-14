# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = [p]
        q1 = [q]
        while q1 and p1:
            q = q1.pop()
            p = p1.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            p1.extend([p.left, p.right])
            q1.extend([q.left, q.right])
        return True