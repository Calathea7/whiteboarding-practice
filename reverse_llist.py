
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:

#         current = head
#         prev_node = None

#         while current:
#             current.next = prev_node
#             prev_node = current
#             current = current.next

#         head = prev_node
#         return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,4,5]
# head is 1
# curr = 1->2->3->4->5
# next = 2->3->4->5
# 1->None
# curr = 2->3->4->5

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        curr = head
        prev = None
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

def contains_cycle(first_node):

    # Check if the linked list contains a cycle

    slow = first_node
    fast = first_node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast is slow:
            return True

    return False
