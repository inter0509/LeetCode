# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseBetween(self, head, m, n):
		"""
		:type head: ListNode
		:type m: int
		:type n: int
		:rtype: ListNode
		"""
		
		if (not head):
			return head;
		if (not head.next):
			return head;
		
		dummy = ListNode(0);
		dummy.next = head;
		prev = dummy; pointer = dummy;
		
		for i in range(m-1):
			prev = prev.next;
		pointer = prev.next;
		
		for i in range(n-m):
			nextNode = pointer.next;
			pointer.next = nextNode.next;
			nextNode.next = prev.next;
			prev.next = nextNode;
		
		return dummy.next;