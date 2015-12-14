class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		
		result = [];
		
		i = 0;
		while(i < len(nums)):
			
			min = nums[i];
			while (i+1) < len(nums) and ((nums[i+1]==nums[i]) or ((nums[i+1]-nums[i])==1)):
				i += 1;
				
					
			if min==nums[i]:
				result.append(str(min));
			else:
				result.append(str(min)+'->'+str(nums[i]));
			
			i += 1;
				
		return result;