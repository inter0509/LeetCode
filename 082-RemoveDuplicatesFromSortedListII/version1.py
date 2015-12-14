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
		
		if not head:
			return head;
		if not head.next:
			return head;
			
		dummy = ListNode(0);
		dummy.next = head;
		# the preview pointer
		preIter = dummy;
		# the current pointer
		currIter = head;
		
		while preIter.next:
			while currIter.next and (preIter.next.val == currIter.next.val): 
				currIter = currIter.next;
			
			# not duplicate pair
			if (currIter == preIter.next):
				preIter = preIter.next;
				currIter = currIter.next;
			# duplicate pair
			else:
				preIter.next = currIter.next;
				
		return dummy.next;