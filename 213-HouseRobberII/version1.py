class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		def robSubArray(subNums):
		
			if (not subNums):
				return 0;
			
			length = len(subNums);
			if (length == 1):
				return subNums[0];
			
			# result[i] indicates the maximum amount of money at house i
			result = [0 for i in range(length)];
			result[0] = subNums[0]
			result[1] = max(subNums[0],subNums[1])
			
			for i in range(2,length):
				result[i] = max(result[i-2]+subNums[i],result[i-1]);
				
			return result[length-1];
		
		if (not nums):
			return 0;
		length = len(nums);
		if (length == 1):
			return nums[0];
		
		max1 = robSubArray(nums[1:]);
		max2 = robSubArray(nums[0:length-1]);
		
		return max(max1,max2);