# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		
		dummy = ListNode(0);
		pointer = dummy;
		
		increase = 0;
		while(l1 or l2):
			add = (l1.val if l1 else 0)+(l2.val if l2 else 0)+increase;
			increase = add/10;
			digit = add%10;
			
			pointer.next = ListNode(digit);
			pointer = pointer.next;
			
			if l1:
				l1 = l1.next;
			if l2:
				l2 = l2.next;
			
		if (increase):
			pointer.next = ListNode(1);
			pointer.next.next = None;
		else:
			pointer.next = None
			
		return dummy.next;