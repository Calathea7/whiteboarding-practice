'''
Write a function that takes in the head of a singly-linked list. It should return True if two nodes with the same data appear consecutively.
Example test cases:
in: 1 → 2 → 2
out: True

in: 1 → 2 → 1
out: False
'''

def consecutive(node):

	current = node

	while current is not None:

		if current.data == current.next.data:
			return True
		else:
			current = current.next

	return False
