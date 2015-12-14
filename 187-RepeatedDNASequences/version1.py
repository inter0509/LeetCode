class Solution(object):
	def findRepeatedDnaSequences(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		
		length = len(s);
		if length < 10:
			return [];
		
		results = [];
		dict = {};
		for i in range(length-10+1):
			subString = s[i:i+10];
			if subString not in dict:
				dict[subString] = 1;
			else:
				if dict[subString] == 1:
					results.append(subString);
				dict[subString] += 1;
				
		return results;