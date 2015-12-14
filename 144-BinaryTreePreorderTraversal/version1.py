# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		
		if not root:
			return [];
			
		pointer = root;
		results = [];
		stack = [];
		
		while stack or pointer:
			if pointer:
				results.append(pointer.val);
				if pointer.right:
					stack.append(pointer.right);
				pointer = pointer.left;
			else:
				pointer = stack.pop();
				
		return results;