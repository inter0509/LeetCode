# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""
		
		temp1 = ListNode(0);
		temp2 = ListNode(0);
		# the list to contain nodes elements that are less than x;
		list1 = temp1;
		# the list to contain nodes elements that are equal or larger than x;
		list2 = temp2;
		pointer = head;
		
		while pointer:
			if (pointer.val < x):
				list1.next = pointer;
				pointer = pointer.next;
				list1 = list1.next;
				list1.next = None;
			else:
				list2.next = pointer;
				pointer = pointer.next;
				list2 = list2.next;
				list2.next = None;
				
		list1.next = temp2.next;
		head = temp1.next;
		
		return head;