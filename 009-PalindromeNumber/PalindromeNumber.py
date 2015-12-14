class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		
		if (x < 0):
			return False;
		base = 1;
		temp = x;
		while(temp >= 10):
			base *= 10;
			temp /= 10;
		
		while(x > 0):
			left = x / base;
			right = x % 10;
			if (left != right):
				return False;
			x = ((x%base)/10);
			base /= 100;
		
		return True;