class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		
		hashSet = {};
		for num in nums:
			if num in hashSet:
				return True;
			hashSet[num] = 1;
			
		return False;