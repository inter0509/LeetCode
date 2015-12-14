# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	
	def sortedListToBST(self, head):
		return self.dfs(head, None)
		
	def dfs(self, head, end):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		
		if head == end:
			return None;
		
		fast = head; slow = head;
		while fast!=end and fast.next!=end:
			fast = fast.next.next;
			slow = slow.next;
			
		newNode = TreeNode(slow.val);
		newNode.left = self.dfs(head,slow);
		newNode.right = self.dfs(slow.next,end);
		
		return newNode;