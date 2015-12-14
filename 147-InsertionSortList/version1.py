# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def insertionSortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		
		if not head or not head.next:
			return head;
		
		# dummy is pre node for the sorted list
		dummy = ListNode(0);
		preHead = dummy;
		
		currentHead = head;
		while (currentHead):
			pointer = dummy;
			
			if currentHead.val > preHead.val:
				pointer = preHead;
			
			while(pointer.next and pointer.next.val <= currentHead.val):
				pointer = pointer.next;
			
			# find the insert position in the sorted list
			
			preHead = currentHead;
			temp = currentHead.next;
			currentHead.next = pointer.next;
			pointer.next = currentHead;
			
			currentHead = temp;
			
		return dummy.next;