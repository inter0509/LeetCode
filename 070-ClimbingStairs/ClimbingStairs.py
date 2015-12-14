class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		
		count = [0]*n;
		for i in range(1,n+1):
			if (i == 1):
				count[i-1] = 1;
			elif (i == 2):
				count[i-1] = 2;
			else:
				count[i-1] = count[i-2]+count[i-3];
				
		return count[n-1];