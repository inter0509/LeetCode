# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		
		if (not head):
			return head;
		elif (not head.next):
			return head;
		
		pointer = head;
		head = self.reverseList(pointer.next); #head->...->...<-pointer
		pointer.next.next = pointer;
		pointer.next = None;
		
		return head;