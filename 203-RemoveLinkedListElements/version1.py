# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		
		if (not head):
			return head;
		
		pointer = head;
		while(pointer.next):
			if (pointer.next.val == val):
				pointer.next = pointer.next.next;
			else:
				pointer = pointer.next;
				
		if (head.val ==  val):
			head = head.next;
		
		return head;