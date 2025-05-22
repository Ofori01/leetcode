# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add the 2 numbers and keep rem
        head = ListNode(0)
        main =head
        rem = 0
        while l1 or l2:
            num = rem
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num+=l2.val
                l2=l2.next
            # better than using string converion
            rem = num // 10
            # update rem 
            
            main.next = ListNode(num % 10)
            main= main.next
        # if rems are left
        if rem >0:
            main.next = ListNode(rem)
        return head.next
            
        