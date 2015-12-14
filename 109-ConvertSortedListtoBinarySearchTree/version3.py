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
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		
		if not nums:
			return None;
			
		mid = len(nums)/2;
		newNode = TreeNode(nums[mid]);
		newNode.left = self.sortedArrayToBST(nums[:mid]);
		newNode.right = self.sortedArrayToBST(nums[mid+1:]);
		
		return newNode;
		
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		
		vect = [];
		pointer = head;
		while pointer:
			vect.append(pointer.val);
			pointer = pointer.next;
			
		return self.sortedArrayToBST(vect);