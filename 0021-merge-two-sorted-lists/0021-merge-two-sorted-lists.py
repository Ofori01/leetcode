# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head= ListNode(0,None)
        main = head
        # move though both lists and compare 
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                main.next = cur1
                cur1 = cur1.next
            else:
                main.next = cur2
                cur2 = cur2.next
            # don't forget to move the main pointer
            main = main.next
        while cur1:
            main.next = cur1
            cur1 = cur1.next
            # don't forget to move the main pointer
            main = main.next
        while cur2:
            main.next = cur2
            cur2 = cur2.next
            # don't forget to move the main pointer
            main= main.next
        return head.next
            