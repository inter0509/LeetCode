class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		if (len(nums) == 0):
			return 0;
			
		lastReach = 0;
		currentReach = 0;
		step = 0;
		
		for i in range(len(nums)):
			
			# the reach cannot be increased
			if (i > currentReach):
				break;
			
			# current step reaches further than last step and update step 
			if (i > lastReach):
				step += 1;
				lastReach = currentReach;
			
			local = nums[i]+i;
			currentReach = max(currentReach,local);
			
		if (currentReach < (len(nums)-1)):
			return 0;
		
		return step;