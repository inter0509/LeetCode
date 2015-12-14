class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		
		def nextHappy(number):
			sum  = 0;
			while(number!=0):
				digit = number%10;
				sum += digit*digit;
				number = number/10;
		
			return sum;
		
		hashSet = {}
		
		while (n!=1):
			n = nextHappy(n);
			if (n in hashSet):
				return False;
			else:
				hashSet[n] = 1;
			
		return True;