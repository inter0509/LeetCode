class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		
		if not nums:
			return [-1, -1];
			
		start = 0; end = len(nums)-1;
		
		while (start <= end):
			mid = (start+end)/2;
			
			if (nums[mid] < target):
				start = mid + 1;
			elif(nums[mid] > target):
				end = mid - 1;
			else:
				result = [mid, mid];
				if (nums[start] == target):
					result[0] = start;
				if (nums[end] == target):
					result[1] = end;
				for i in range(mid,end+1):
					if (nums[i] != target):
						result[1] = i-1;
						break;
				for i in range(mid,start-1,-1):
					if (nums[i] != target):
						result[0] = i+1;
						break;
						
				return result;
		
		return [-1,-1]