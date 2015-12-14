class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		
		stack = [];
		
		for i in s:
			if (i == '(' or i == '[' or i == '{'):
				stack.append(i);
		
			if (i == ')'):
				if not stack or stack.pop() != '(':
					return False;
	
						
			if (i == ']'):
				if not stack or stack.pop() != '[':
					return False;
						
			if (i == '}'):
				if not stack or stack.pop() != '{':
					return False;
			
			
		if not stack:
			return True;
		else:
			return False;