# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # 1 2 3 4 5 6 7 8
    #       -
    # -       - 
        dummy = ListNode(0, head)
        first, second = dummy, dummy
        for _ in range(n+1):
            first = first.next
            # n -= 1
        # second = ListNode(0, head)
        # dummy = dummy.next
        while first:
            second = second.next
            first = first.next
        print(second.val)
        # temp = second.next
        second.next = second.next.next
        return dummy.next