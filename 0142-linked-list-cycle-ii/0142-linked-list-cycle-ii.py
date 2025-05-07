# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # make fast and slow move. fast twice as fast. Then when fast and slow meets. move slow to head and move them one step a time. and return where they meet. Floyd cycle i think

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None
        # when cycle detected
        slow = head

        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
        