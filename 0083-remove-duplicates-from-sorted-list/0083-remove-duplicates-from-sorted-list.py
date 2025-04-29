# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow =head

        while fast:
            # move fast until different element
            while fast and  fast.val == slow.val:
                fast = fast.next
            # then link slow with fast
            slow.next = fast
            slow = fast
        
        return head