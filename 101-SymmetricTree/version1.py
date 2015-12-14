# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		
		def SymmetricLeftRight(left,right):
			if ((not left) and (not right)):
				return True
			
			if (left and right):
				return ((left.val==right.val) and SymmetricLeftRight(left.right,right.left) and SymmetricLeftRight(left.left,right.right));
				
			return False;
		
		if not root:
			return True;
		
		return SymmetricLeftRight(root.left,root.right);