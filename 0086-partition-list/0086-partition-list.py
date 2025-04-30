# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # add lesser to a different list
        lesser = ListNode(0)
        l = lesser
        # add greater to a different list
        greater = ListNode(0)
        g = greater
        cur = head

        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                g.next = cur
                g = g.next
            cur= cur.next

        g.next = None
        l.next = greater.next
        return lesser.next




        

        
        