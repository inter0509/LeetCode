class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		
		if (len(strs) == 0):
			return ''
		if (len(strs) == 1):
			return strs[0];
		
		result = '';
		
		# strs[i][j]
		for j in range(len(strs[0])):
			for i in range(len(strs)):
				if ((j >= len(strs[i])) or (strs[i][j] != strs[0][j])):
					return result;
			result += strs[0][j];
				
		return result;