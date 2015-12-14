import sys

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		length = len(nums);
		if (length == 0):
			return 0;
			
		maxSum = -sys.maxint;
		currentSum = 0;
		for i in range(length):
			
			#the subarray that includes element nums[i]
			currentSum += nums[i];
			maxSum = max(maxSum, currentSum);
			
			# if currentSum is negative, it means that this part can be discarded so that we can achieve larger sum later
			if (currentSum < 0):
				currentSum = 0;
				
		return maxSum;