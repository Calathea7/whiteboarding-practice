# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        current = head
        prev_node = None

        while current:
            current.next = prev_node
            prev_node = current
            current = current.next

        head = prev_node
        return prev_node
