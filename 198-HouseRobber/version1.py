class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		if (not nums):
			return 0;
		
		length = len(nums);
		if (length == 1):
			return nums[0];
		
		# result[i] indicates the maximum amount of money at house i
		result = [0 for i in range(length)];
		result[0] = nums[0]
		result[1] = max(nums[0],nums[1])
		
		for i in range(2,length):
			result[i] = max(result[i-2]+nums[i],result[i-1]);
			
		return result[length-1];