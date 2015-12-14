# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		
		# first find the mid node of the list
		if(not head):
			return True;
		elif (not head.next):
			return True
			
		fast = head; slow = head;
		while (fast.next and fast.next.next):
			slow = slow.next;
			fast = fast.next.next;
		
		current = slow.next;
		while(current.next):
			nextNode = current.next;
			current.next = nextNode.next;
			nextNode.next = slow.next;
			slow.next = nextNode;
			
		pointer1 = head; pointer2 = slow.next;
		while(pointer2):
			if (pointer1.val != pointer2.val):
				return False;
			pointer1= pointer1.next;
			pointer2 = pointer2.next;
			
		return True;