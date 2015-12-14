class Solution(object):
	
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
		ret = [];
		nums.sort();
		
		self.dfs(nums, 0, [], ret);
		
		return ret;
	
	def dfs(self, nums, pos, currList, results):
		
		if not currList in results:
			results.append([]+currList);
		
		for i in range(pos, len(nums)):
			currList.append(nums[i]);
			self.dfs(nums, i+1, currList, results);
			currList.pop();