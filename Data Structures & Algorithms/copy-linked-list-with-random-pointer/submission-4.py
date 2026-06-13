"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldCopy = {}
        cur = head
        while cur:
            oldCopy[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            
            try:
                oldCopy[cur].next = oldCopy[cur.next]
            except:
                oldCopy[cur].next = None
            try:
                oldCopy[cur].random = oldCopy[cur.random]
            except:
                oldCopy[cur].random = None
            cur = cur.next
        print(oldCopy)
        try:
            return oldCopy[head]
        except:
            return None