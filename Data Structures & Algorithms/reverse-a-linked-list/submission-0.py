# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        while head.next is not None:
            nextVal = head.next
            head.next = prev
            prev = head
            head = nextVal
        head.next = prev
        return head
