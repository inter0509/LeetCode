class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		
		strList = s.strip().split();
		length = len(strList);
		
		if (length == 0):
			return 0;
			
		
		return len(strList[-1]);