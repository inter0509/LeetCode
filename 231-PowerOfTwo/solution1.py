class Solution(object):
	def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if (n < 1):
			return False;
		elif (n == 1):
			return True;
		else:
			while (n != 1):
				if ((n%2) != 0):
					return False
				n /= 2;
			return True;