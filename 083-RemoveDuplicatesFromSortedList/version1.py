# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		
		if (head == None):
			return head
		else:
			pointer = head;
			current = head.val;
		
		while(pointer != None):
			if (pointer.next != None):
				if (pointer.next.val == pointer.val):
					pointer.next = pointer.next.next;
				else:
					pointer = pointer.next;
			else:
				pointer = pointer.next;
				
		return head;