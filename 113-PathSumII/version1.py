# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: List[List[int]]
		"""
		
		# currentSum: int, current sum of path
		# Path: list, current path
		def pathSumWithSet(root, currentSum, Path):
			
			if ((not root.left) and (not root.right)):
				if (currentSum == sum):
					result.append(Path);
			
			if (root.left):
				pathSumWithSet(root.left,currentSum+root.left.val,Path+[root.left.val]);
			if (root.right):
				pathSumWithSet(root.right,currentSum+root.right.val,Path+[root.right.val]);
			
		if not root:
			return [];
		
		result = [];
		pathSumWithSet(root,root.val,[root.val]);
		return result;