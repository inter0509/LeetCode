class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		
		length1 = len(haystack);
		length2 = len(needle);
		
		index = -1;
		
		if (length1 == 0 and length2 == 0):
			index = 0;
		
		for i in range(0,(length1-length2+1)):
			j = 0;
			while (j < length2):
				if (haystack[i+j] != needle[j]):
					break;
				j += 1;
					
			if (j == length2):
				index = i;
				break;
				
		return index;