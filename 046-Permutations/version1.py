class Solution(object):
	
	def dfs(self, nums, visited, currList, result):
		if len(currList) == len(nums):
			result.append([]+currList);
			return;
			
		for i in range(len(nums)):
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
	
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
		result = [];
		visited = [None for i in range(len(nums))];
		nums.sort();
		self.dfs(nums, visited, [], result);
		return result;
