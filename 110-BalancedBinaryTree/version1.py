# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
			
		def maxDepth(root):
			if not root:
				return 0;
			
			return max(maxDepth(root.left),maxDepth(root.right))+1;
			
		if not root:
			return True;
			
		leftHeight = maxDepth(root.left);
		rightHeight = maxDepth(root.right);
		
		if ((leftHeight-rightHeight)>1 or (rightHeight-leftHeight)>1):
			return False
		else:
			return self.isBalanced(root.left) and self.isBalanced(root.right);
		