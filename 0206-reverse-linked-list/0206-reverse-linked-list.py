# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a None node and for each head make it's next the Node
        node = None
        while head:
            temp = head.next
            head.next = node
            node= head
            head = temp
        return node
        