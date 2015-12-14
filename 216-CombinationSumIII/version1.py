class Solution(object):
	
	def dfs(self, k, target, pos, current, results):
		if target < 0:
			return;
			
		if len(current) == k:
			if target == 0:
				results.append([]+current);
			return 
			
		for i in range(pos, 10):
			current.append(i);
			self.dfs(k, target-i, i+1, current, results);
			current.pop();
	
	def combinationSum3(self, k, n):
		"""
		:type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		
		results = [];
		self.dfs(k, n, 1, [], results);
		return results;
		