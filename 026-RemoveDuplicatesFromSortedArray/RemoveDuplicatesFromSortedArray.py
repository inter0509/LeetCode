class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		pointer =0; # indicate the position of non-duplicate element
		if (len(nums) == 0):
			return 0;
			
		for i in range(1,len(nums)):
			if (nums[pointer] != nums[i]):
				pointer += 1;
				nums[pointer] = nums[i];
		return (pointer+1);