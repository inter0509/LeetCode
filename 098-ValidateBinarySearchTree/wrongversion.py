# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
This is not a correct solution.
This solution only compare the left/right node values to its father node,
but it cannot guarantee the node value requirements for its grandfather nodes 
'''

class Solution(object):
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		
		if not root:
			return True;
			
		if (root.left):
			if not(root.left.val < root.val):
				return False;
		
		if (root.right):
			if not (root.right.val > root.val):
				return False;
		
		return (self.isValidBST(root.left) and self.isValidBST(root.right)); 