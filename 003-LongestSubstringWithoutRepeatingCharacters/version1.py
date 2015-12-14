class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		
		dict = {};
		start = 0;
		result = 0;
		length = len(s);
		
		if length <= 1:
			return length;
		
		for letter in s:
			dict[letter] = -1;
		
		for i in range(length):
			if dict[s[i]] >= start:
				start = dict[s[i]]+1;
			result = max(result,i-start+1);
			dict[s[i]] = i;
			
		
		return result;