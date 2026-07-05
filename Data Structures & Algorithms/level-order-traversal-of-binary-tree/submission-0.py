# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        queue.append(root)
        final = []
        while queue:
            qlen = len(queue)
            current = []    
            for i in range(qlen):
                node = queue.pop(0)
                if node:
                    current.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if current:
                final.append(current)
        return final
