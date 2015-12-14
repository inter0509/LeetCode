# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sumNumbers(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		
		def PathNumber(root,currentSum):
			if not root:
				return 0;
			
			currentSum = currentSum*10+root.val;
			if ((not root.left) and (not root.right)):
				return currentSum;
			
			return PathNumber(root.left,currentSum)+PathNumber(root.right,currentSum);
		
		return PathNumber(root,0);