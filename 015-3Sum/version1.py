class Solution(object):
	
	def twoSum(self, sortedNums, target):
		results = [];
		left = 0; right = len(sortedNums)-1;
		while (left < right):
			sum = sortedNums[left]+sortedNums[right];
			if sum < target:
				left += 1;
			elif sum > target:
				right -= 1;
			else:
				results.append([sortedNums[left],sortedNums[right]]);
				
				temp = left + 1;
				while temp < right and sortedNums[temp] == sortedNums[left]:
					temp += 1;
				left = temp;
				
				temp = right - 1;
				while temp > left and sortedNums[temp] == sortedNums[right]:
					temp -= 1;
				right = temp;
				
		return results;
				
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
		results = [];
		length = len(nums);
		if length < 3:
			return results;
		
		nums.sort();
		i = 0;
		while i < (length-2):
			
			if i>0 and nums[i]==nums[i-1]:
				i += 1;
				continue
				
			target = 0 - nums[i];
			twoSumResult = self.twoSum(nums[i+1:], target);
			if twoSumResult:
				for j in range(len(twoSumResult)):
					results.append([nums[i]]+twoSumResult[j]);
			i += 1
		return results;
			

s = Solution();
print s.threeSum([0,0,0,0]);