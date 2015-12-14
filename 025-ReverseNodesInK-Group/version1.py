# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	
	def reverseList(self, start, end):
		'''
		: reverse sub list given the start and end node
		'''
		temp = ListNode(0);
		temp.next = start;
		
		while temp.next != end:
			nextNode = start.next;
			start.next = nextNode.next;
			nextNode.next = temp.next;
			temp.next = nextNode;
			
		return end, start;
		
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		
		if k < 2:
			return head;
			
		if not head or not head.next:
			return head;
			
		dummy = ListNode(0);
		dummy.next = head;
		start = dummy;
		
		while start.next:
			end = start;
			for i in range(k-1):
				# get k nodes
				end = end.next;
				# do not reverse if the number of remaining node is less than k 
				if not end.next:
					return dummy.next
					
			temp1,temp2 = self.reverseList(start.next, end.next);
			start.next = temp1;
			start = temp2;
		
		return dummy.next;
		