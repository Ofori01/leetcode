# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast and slow pointers
        # fast moves twice
        # slow moves once. At the point fast can't move slow is at the midpoint
        fast = slow = head
        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next
        return slow