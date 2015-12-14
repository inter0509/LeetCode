# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution(object):
	
	def BSThelper(self, r, min, max):
		if not r:
			return True;
			
		if r.val <= min or r.val >= max:
			return False;
			
		return self.BSThelper(r.left, min, r.val) and self.BSThelper(r.right, r.val, max);
	
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
			
		return self.BSThelper(root, -sys.maxint, sys.maxint);