# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque;

class Solution(object):
	
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if (root == None):
			return [];
		
		result = [];
		NodeDeque = deque();
		NodeDeque.append(root);
		
		
		while(NodeDeque):
			temp = [];
			num = len(NodeDeque);
			
			for i in range(num):
				node = NodeDeque.popleft();
				if (node):
					temp.append(node.val);
					NodeDeque.append(node.left);
					NodeDeque.append(node.right);
			
			if (temp):
				result.append(temp);
				
		return result;