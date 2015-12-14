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
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		if not head:
			return None;
		
		length = 0;
		pointer = head;
		while pointer:
			length += 1;
			pointer = pointer.next;
		
		# list is mutable for argument reference
		return self.dfs([head],0,length-1);
		
	def dfs(self, head, start, end):
		'''
		: elements order in the sorted list corresponds to the binary search tree (in order traversal).
		: So, we seek a in order build of the BST in a bottom-up way
		'''
		
		print start,end;
		
		if start > end:
			return None;
		
		mid = (start+end)/2;
		leftNode = self.dfs(head, start, mid-1);
		newNode = TreeNode(head[0].val);
		
		head[0] = head[0].next;
		rightNode = self.dfs(head, mid+1,end);
		newNode.left = leftNode;
		newNode.right = rightNode;
		
		return newNode;