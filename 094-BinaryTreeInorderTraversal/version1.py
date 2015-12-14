# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		
		result = [];
		if (not root):
			return result;
			
		pointer = root;
		stack = [];
		
		while(pointer or stack):
			
			while(pointer):
				stack.append(pointer);
				pointer = pointer.left;
			
			
			if (stack):
				pointer = stack.pop();
				result.append(pointer.val);
				pointer = pointer.right;
				
		return result;