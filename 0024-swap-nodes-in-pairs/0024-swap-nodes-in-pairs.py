# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0)
        dummy.next  = head
        cur = dummy
        
        while cur.next and cur.next.next:
            # swap by taking cur and cur.next.next
            A = cur.next
            B = cur.next.next
            cur.next = B
            A.next = B.next
            B.next = A
            cur = A
        return dummy.next
