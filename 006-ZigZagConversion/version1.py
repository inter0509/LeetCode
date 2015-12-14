class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		
		if numRows == 1 or not s:
			return s;
			
		ZigSize = 2*numRows - 2;
		dict = {};
		for i in range(numRows):
			dict[i] = '';
			
		for i in range(len(s)):
			remains = i%ZigSize;
			if remains >= numRows:
				remains = ZigSize - remains;
			dict[remains] += s[i];
			
		results = '';
		for i in range(numRows):
			results += dict[i];
			
		return results;