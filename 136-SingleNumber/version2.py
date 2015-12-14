class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		# bitwise operations:
		# :x^x = 0; x^0=x;
		ans = 0;
		for num in nums:
			ans = ans ^ num;
			
		return ans;