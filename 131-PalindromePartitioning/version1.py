class Solution(object):
	
	def isPalindrome(self, s):
		if not s:	
			return True;
		left = 0; right = len(s)-1;
		while left < right:
			if s[left] == s[right]:
				left += 1;
				right -= 1;
			else:
				return False
				
		return True;
		
	def dfs(self, s, currResult, results):
		if not s:
			results.append([]+currResult);
			return;
			
		for i in range(1,len(s)+1):
			if self.isPalindrome(s[:i]):
				self.dfs(s[i:],currResult+[s[:i]],results);
	
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		
		results = [];
		self.dfs(s, [], results);
		
		return results;