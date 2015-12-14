# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
		
	
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		
		if not root:
			return 0;
		
		stack = [];
		pointer = root;
		
		while (pointer or stack):
			
			while (pointer):
				stack.append(pointer);
				pointer = pointer.left;
				
			if stack:
				pointer = stack.pop();
				
				# we do not need to traverse the whole tree, we just need to extract value of the number k node using inorder traversal.
				k -= 1;
				if k == 0:
					break;
					
				pointer = pointer.right;
				
		return pointer.val;