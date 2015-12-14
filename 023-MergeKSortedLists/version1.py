# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		
		dummy = ListNode(0);
		pointer = dummy;
		
		while(l1 and l2):
			if (l1.val <= l2.val):
				pointer.next = l1;
				l1 = l1.next;
				pointer = pointer.next;
			else:
				pointer.next = l2;
				l2 = l2.next;
				pointer = pointer.next;
		
		if (l1):
			pointer.next = l1;
		else:
			pointer.next = l2;
			
		return dummy.next;
	
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		
		length = len(lists);
		if (length == 0):
			return None;
		
		while (length > 1):
			k = (length+1)/2;
			for i in range(0,length/2):
				lists[i] = self.mergeTwoLists(lists[i],lists[i+k]);
			length = k;
			
		return lists[0];