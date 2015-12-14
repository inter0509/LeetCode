class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
	
		start = 0;
		end = len(nums)-1;
		
		while (start<=end):
			mid = (start+end)/2;
			
			if (nums[mid] == target):
				return True;
			else:
				if (nums[mid] < nums[end]): # the right half is sorted
					if ((nums[mid]<target) and (nums[end]>=target)):
						start = (mid+1);
					else:
						end = (mid-1);
				elif (nums[mid] > nums[end]):
					if ((nums[mid]>target) and (nums[start]<=target)):
						end = (mid-1);
					else:
						start = (mid+1);
				else:
					end -= 1;
		
		return False;