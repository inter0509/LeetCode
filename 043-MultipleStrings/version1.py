class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		
		# reverse two strings
		num1 = num1[::-1];
		num2 = num2[::-1];
		
		len1 = len(num1); len2 = len(num2);
		multi = [0]*(len1+len2);
		
		for iter1 in range(len1):
			for iter2 in range(len2):
				multi[iter1+iter2] += int(num1[iter1])*int(num2[iter2]);
			
		result = [];
		add = 0;
		for iter in range(len(multi)):
			remain = (multi[iter]+add)%10;
			add = (multi[iter]+add)/10;
			result.append(str(remain));
		
		result = result[::-1];
		while ((len(result)>1) and result[0] == '0'):
			del result[0]
		
		return ''.join(result);