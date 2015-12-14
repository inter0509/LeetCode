class Solution(object):
	def isUgly(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		
		if (num <= 0):
			return False;
		
		for factor in [2,3,5]:
			flag = num%factor;
			while(not flag):
				num = num/factor;
				flag = num%factor;
		
		if (num == 1):
			return True;
		else:
			return False;