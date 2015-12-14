class Solution(object):	
	def centerExpand(self,s,index1,index2):
		left = index1;
		right = index2;
		
		while((left >= 0) and (right < len(s)) and (s[left] == s[right])):
			left -= 1;
			right += 1;
		
		return s[left+1:right];
		
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		
		length = len(s);
		result = '';
		if (length == 0):
			return result;
		
		for i in range(0,length):
			temp = self.centerExpand(s,i,i);
			if (len(temp) > len(result)):
				result = temp;
			temp = self.centerExpand(s,i,i+1);
			if (len(temp) > len(result)):
				result = temp;
				
		return result;
	
