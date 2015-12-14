# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		
		if (not head):
			return head;
		if (not head.next):
			return head
			
		dummy = ListNode(0);
		prev = dummy;
		pointer = head;
		
		while (pointer and pointer.next):
			nextNode = pointer.next;
			pointer.next = nextNode.next;
			nextNode.next = pointer;
			prev.next = nextNode;
			
			prev = pointer;
			pointer = pointer.next;
		
		return dummy.next;