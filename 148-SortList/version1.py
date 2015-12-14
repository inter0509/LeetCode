# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
		
	def merge(self, list1, list2):
		
		if (not list1 and not list2):
			return None;
		elif (not list1):
			return list2;
		elif (not list2):
			return list1;
		
		dummy = ListNode(0);
		pointer = dummy;
		
		while(list1 and list2):
			if (list1.val <= list2.val):
				pointer.next = list1;
				list1 = list1.next;
				pointer = pointer.next;
			else:
				pointer.next = list2;
				list2 = list2.next;
				pointer = pointer.next;
		
		if (list1):
			pointer.next = list1;
		else:
			pointer.next = list2;
			
		return dummy.next;
		
	
	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if (not head):
			return head;
		elif (not head.next):
			return head;
			
		slow = head;
		fast = head.next;
		
		while(fast.next and fast.next.next):
			slow = slow.next;
			fast = fast.next.next;
			
		fast = slow.next;
		# set the tail for the left half list
		slow.next = None; 
		
		left = self.sortList(head);
		right = self.sortList(fast);
		return self.merge(left,right);