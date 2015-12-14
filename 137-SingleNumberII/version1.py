class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		dict = {};
		for num in nums:
			if num in dict:
				dict[num] += 1
			else:
				dict[num] = 1;
				
		for key in dict:
			if dict[key] != 3:
				return key;