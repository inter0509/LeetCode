class Solution(object):
	
	def dfs(self, candidates, target, pos, current, results):
		
		if target < 0:
			return;
		
		if target == 0:
			results.append([]+current);
			return;
		
		for i in range(pos, len(candidates)):
			current.append(candidates[i]);
			self.dfs(candidates, target-candidates[i], i, current, results);
			current.pop();
	
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		
		candidates.sort();
		results = [];
		self.dfs(candidates, target, 0, [], results);
		
		return results;