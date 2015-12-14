# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	
	def DFS(self, root, level):
		if level in Solution.levelDic:
			Solution.levelDic[level].append(root.val);
		else:
			Solution.levelDic[level] = [root.val];
		
		if (root.left):
			self.DFS(root.left,level+1);
		if (root.right):
			self.DFS(root.right,level+1);
	
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		result = [];
		Solution.levelDic = {};
		
		if (root == None):
			return [];
		
		self.DFS(root,0);
		sortedLevels = sorted(Solution.levelDic.keys());
		for lvl in sortedLevels:
			result.append(Solution.levelDic[lvl]);
			
		return result;