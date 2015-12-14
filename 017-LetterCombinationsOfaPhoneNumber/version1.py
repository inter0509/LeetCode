class Solution(object):
	
	def dfs(self, digits, numbers, current, results):
		if len(digits) == 0:
			results.append(''+current);
			return;
		
		digit = int(digits[0])-1;
		for i in range(0, len(numbers[digit])):
			current += str(numbers[digit][i]);
			self.dfs(digits[1:], numbers, current, results);
			current = current[:len(current)-1];
	
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		
		if not digits:
			return [];
			
		numbers = [[],['a','b','c'],['d','e','f'],['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']];
		results = [];
		self.dfs(digits, numbers, '', results);
		return results;