class NumArray(object):
	def __init__(self, nums):
		"""
		initialize your data structure here.
		:type nums: List[int]
		"""
		
		# [)
		self.sums = [0 for i in range(len(nums)+1)];
		for i in range(1,len(nums)+1):
			self.sums[i] = self.sums[i-1]+nums[i-1];
	
	def sumRange(self, i, j):
		"""
		sum of elements nums[i..j], inclusive.
		:type i: int
		:type j: int
		:rtype: int
		"""
		
				
		return self.sums[j+1]-self.sums[i];


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)