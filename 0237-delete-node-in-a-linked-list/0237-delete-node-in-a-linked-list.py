# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # swap the val of the current node with the next
        # then the cur node points to the next 2 to lose the middle node
        node.val  = node.next.val
        node.next= node.next.next