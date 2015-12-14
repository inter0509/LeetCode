class Solution(object):
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		
		results = [];
		length = len(nums);
		if length < 4:
			return []; 
		
		nums.sort();
		dict = {};
		for i in range(length):
			for j in range(i+1,length):
				sum = nums[i]+nums[j];
				if sum in dict:
					dict[sum].append([i,j]);
				else:
					dict[sum] = [[i,j]]
		
		i = 0;
		while i < (length-3):
			if i>0 and nums[i]==nums[i-1]:
				i += 1;
				continue;
				
			j = i+1;
			while j < (length-2):
				if j > (i+1) and nums[j]==nums[j-1]:
					j += 1;
					continue;
					
				targ = target-nums[i]-nums[j];
				lastInput = [];
				if targ in dict:
					for k in range(len(dict[targ])):
						index = dict[targ][k];
						if index[0] <= j:
							continue;
							
						# avoid duplicates of the last two elements
						if not lastInput or [nums[index[0]],nums[index[1]]] != [nums[lastInput[0]],nums[lastInput[1]]]:
							results.append([nums[i],nums[j],nums[index[0]],nums[index[1]]]);
							lastInput = index;
				j += 1;
			
			i += 1;
			
		return results;