# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		
		def binaryTreeWithPath(root,path,paths):
			if (not root):
				return [];
			path += str(root.val);
			if ((not root.left) and (not root.right)):
				paths.append(path);
			
			binaryTreeWithPath(root.left,path+'->',paths);
			binaryTreeWithPath(root.right,path+'->',paths);
		
		result = []
		binaryTreeWithPath(root,'',result);
		return result;