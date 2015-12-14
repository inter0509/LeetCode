class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		
		hashSet = {};
		for i in range(len(nums)):
			if nums[i] in hashSet:
				index = hashSet.get(nums[i]);
				diff = i - index;
				if (diff <= k):
					return True
			hashSet[nums[i]] = i;
			
		
		return False;