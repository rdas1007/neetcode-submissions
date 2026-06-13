# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        added = dummy
        carry = 0
        while l1 or l2 or carry:
            a = 0 if l1 is None else l1.val
            b = 0 if l2 is None else l2.val
            sum_val = a + b + carry
            value = sum_val % 10
            carry = sum_val // 10
            added.next = ListNode(value)
            # new = ListNode(0)
            # added.next = new
            added = added.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

