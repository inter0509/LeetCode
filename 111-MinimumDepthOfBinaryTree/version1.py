# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque;

class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		
		if not (root):
			return 0;
			
		NodeDeque = deque([(root,1)]);

		while (NodeDeque):
			node, level = NodeDeque.popleft()
			if node:
				if not node.left and not node.right:
					return level;
				else:
					NodeDeque.append((node.left,level+1));
					NodeDeque.append((node.right,level+1));