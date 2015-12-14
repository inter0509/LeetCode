class Solution:
	def combine(self, n, k):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
		ret = [];
		self.dfs(n, k, 1, [], ret);
		
		return ret;
	
	def dfs(self, n, k, pos, currList, results):
		
		if (len(currList) == k):
			results.append([]+currList);
			return
		
		for i in range(pos, n+1):
			currList.append(i);
			self.dfs(n, k, i+1, currList, results);
			currList.pop();