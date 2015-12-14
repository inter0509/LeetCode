class Solution(object):
	
	def dfs(self, candidates, target, pos, current, results):
		
		if target < 0:
			return;
		
		if target == 0:
			results.append([]+current);
			return;
		
		i = pos;
		while i < len(candidates):
			current.append(candidates[i]);
			
			# each element can only be used once. So, the pos starts from (i+1) rather than i
			self.dfs(candidates, target-candidates[i], i+1, current, results);
			current.pop();
			
			while i<(len(candidates)-1) and (candidates[i]==candidates[i+1]):
				i += 1;
				
			i += 1;
	
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		
		candidates.sort();
		results = [];
		self.dfs(candidates, target, 0, [], results);
		
		return results;