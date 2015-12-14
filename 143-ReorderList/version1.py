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
	
	def reorderList(self, head):
		"""
		:type head: ListNode
		:rtype: void Do not return anything, modify head in-place instead.
		"""
		
		if not head:
			return;
		if not head.next:
			return;
		if not head.next.next:
			return;
		
		# step 1: split the linked list into two parts
		fast = head; slow = head;
		while(fast and fast.next):
			fast = fast.next.next;
			slow = slow.next;
		head1 = head;
		head2 = slow.next;
		# mark the end of the first list
		slow.next = None; 
		
		# step 2: reverse the second list
		head2 = self.reverseList(head2);
		'''
		dummy = ListNode(0);
		dummy.next = head2;
		pointer = head2;
		while(pointer.next):
			nextNode = pointer.next;
			pointer.next = nextNode.next;
			nextNode.next = dummy.next;
			dummy.next = nextNode;
		head2 = dummy.next;
		'''
		
		# merge two lists
		iter1 = head1; iter2 = head2;
		while (iter2):
			temp1 = iter1.next;
			temp2 = iter2.next;
			iter1.next = iter2;
			iter2.next = temp1;
			iter1 = temp1;
			iter2 = temp2;