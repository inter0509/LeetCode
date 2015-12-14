# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		
		if not root or root == p or root == q:
			return root;
			
		leftNode = self.lowestCommonAncestor(root.left, p, q);
		rightNode = self.lowestCommonAncestor(root.right, p, q);
		
		# p,q分别在root左右两侧，满足条件
		if leftNode and rightNode:
			return root;
		elif not leftNode:
			return rightNode;
		else:
			return leftNode;