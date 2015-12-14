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
			
		dummy = ListNode(0);
		dummy.next = head;
		pointer = head;
		
		while(pointer.next):
			nextNode = pointer.next;
			pointer.next = nextNode.next;
			nextNode.next = dummy.next;
			dummy.next = nextNode;
			
		return dummy.next; 
		