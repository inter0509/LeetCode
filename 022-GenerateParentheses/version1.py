class Solution(object):
	
	def dfs(self, leftParenNumber, rightParenNumber, current, results):
	
		if leftParenNumber == 0 and rightParenNumber == 0:
			results.append(''+current);
			return;
		
		# we can add the left parenthesis if we still have left parenthesis
		if (leftParenNumber > 0):
			current += '(';
			self.dfs(leftParenNumber-1, rightParenNumber, current, results);
			current = current[:len(current)-1];
		
		# we can add the right parenthesis if we have more right parenthesis
		if (leftParenNumber < rightParenNumber):
			current += ')';
			self.dfs(leftParenNumber, rightParenNumber-1, current, results);
			current = current[:len(current)-1];
	
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		
		results = [];
		self.dfs(n, n, '', results);
		return results;