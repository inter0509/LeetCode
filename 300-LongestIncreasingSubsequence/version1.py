class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		if not nums:
			return 0;
		length = len(nums);
		
		# vect[i] indicates the length of the longest increasing subsequence of end at nums[i];
		vect = [1 for i in range(length)];
		maxLen = 1;
		
		for i in range(1, length):
			for j in range(i-1,-1,-1):
				if (nums[i] > nums[j]):
					vect[i] = max(vect[i],vect[j]+1);
			if maxLen < vect[i]:
				maxLen = vect[i];
				
		return maxLen;
		
s  = Solution();
print s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]);