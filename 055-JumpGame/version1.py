class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		
		if (len(nums) == 0):
			return False
			
		reach = 0;
		
		for i in range(len(nums)):
			
			# the reach cannot be increased
			if (i > reach):
				break;
			
			local = nums[i]+i;
			reach = max(reach,local);
			
		if (reach < (len(nums)-1)):
			return False;
		
		return True;