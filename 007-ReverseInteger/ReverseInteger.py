class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		
		Negetive = False;
		if (x < 0):
			Negetive = True; 
			x = - x;
		
		y = 0;
		while( x != 0):
			remain = x % 10;
			x = x / 10;
			
			y = y*10 + remain;
			
			if (y > 2147483647):
				return 0;
		
		if (Negetive ==  True):
			y = -y;
			
		return y;
