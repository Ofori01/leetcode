# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # new idea. Use fast and slow pointers
        # basically assume n steps between fast and slow and move them till the end while maintianing the steps. the slow would be on the element to used for the deletion not the element to delete
        # also if fast goes to end immediately after n steps, it means the head has to go
        slow = fast = head

        for _ in range(n):
            fast = fast.next
        # when n= len(list) fast = None
        
        if not fast:
            head  = head.next
            return head
        # if fast is a node
        while fast.next:
            fast = fast.next
            slow=slow.next
        slow.next = slow.next.next
        return head
