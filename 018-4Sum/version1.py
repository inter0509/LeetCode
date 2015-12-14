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
			return results;
			
		nums.sort();
		
		i = 0;
		while i < (length-3):
			# remove duplicates of the first element;
			if i > 0 and nums[i]==nums[i-1]:
				i += 1;
				continue;
				
			j = i+1;
			while j < (length-2):
				# remove duplicates of the second element;
				if j > (i+1) and nums[j]==nums[j-1]:
					j += 1;
					continue;
			
				remainTarget = target-nums[i]-nums[j];
				left = j+1; right=length-1;
				while left<right:
					sum = nums[left]+nums[right];
					if sum < remainTarget:
						left += 1;
					elif sum > remainTarget:
						right -= 1;
					else:
						results.append([nums[i],nums[j],nums[left],nums[right]]);
						
						tempIndex = left+1;
						while tempIndex < right and nums[tempIndex]==nums[left]:
							tempIndex += 1;
						left = tempIndex;
						
						tempIndex = right -1;
						while tempIndex > left and nums[tempIndex]==nums[right]:
							tempIndex -= 1;
						right = tempIndex;
				
				j += 1;
						
			i += 1;
					
		return results;
		
s = Solution();
print s.fourSum([1,0,-1,0,-2,2],0);