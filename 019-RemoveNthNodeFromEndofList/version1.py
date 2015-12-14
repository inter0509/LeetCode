# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		
		dummy = ListNode(0);
		dummy.next = head;
		
		pointer1 = dummy; pointer2 = dummy;
		
		for i in range(n):
			pointer1 = pointer1.next;
			
		while(pointer1.next):
			pointer1 = pointer1.next;
			pointer2 = pointer2.next;

		pointer2.next = pointer2.next.next;

		
		return dummy.next;