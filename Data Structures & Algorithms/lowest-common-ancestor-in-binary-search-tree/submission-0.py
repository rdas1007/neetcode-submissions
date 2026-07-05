# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        left = False
        right = False
        def found(root):
            nonlocal left, right, lca
            # print(root.left, root.right, p.val, q.val)
            if root.val > p.val and root.val > q.val:
                found(root.left)
            elif root.val < q.val and root.val < p.val:
                found(root.right)
            else:
                lca = root
        found(root)
        return lca
            
            