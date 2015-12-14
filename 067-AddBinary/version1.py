class Solution(object):
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		
		len1 = len(a); len2 = len(b);
		if (len1 >= len2):
			for i in range(len1-len2):
				b = '0'+b;
		else:
			for i in range(len2 - len1):
				a = '0'+a;
		
		flag = 0;
		
		print a,b
		
		result = '';
		for i in range(max(len1,len2)-1,-1,-1):
			sum = int(a[i])+int(b[i])+flag;
			flag = sum/2;
			newStr = sum%2;
			result = str(newStr)+result;
			
		if (flag == 1):
			result = '1'+result;
			
		return result;