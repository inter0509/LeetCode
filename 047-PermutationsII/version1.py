class Solution(object):
	
	def dfs(self, nums, visited, currList, result):
		if len(currList) == len(nums):
			if not currList in result:
				result.append([]+currList);
			return;
		
		i = 0;
		while i < len(nums):
			'''
			: There are two differences compared with the subset problem
			: 1.) the for loop iterates every element rather than starting with pos variable
			: 2.) we use the visited[] to mark the used elements
			'''
			if not visited[i]:
				# the ith element has been used in the currList
				visited[i] = True;
				currList.append(nums[i]);
				self.dfs(nums, visited, currList, result);
				visited[i] = False;
				currList.pop();
				while i<(len(nums)-1) and (nums[i]==nums[i+1]):
					i += 1;
				
				
			i += 1;
	
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
		result = [];
		visited = [None for i in range(len(nums))];
		nums.sort();
		self.dfs(nums, visited, [], result);
		return result;
