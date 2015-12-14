class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		
		strList = str.strip().split();
		if not strList:
			return False;
		if len(strList) != len(pattern):
			return False;
		
		dict1 = {};
		dict2 = {};
		for i in range(len(strList)):
			if strList[i] not in dict1:
				dict1[strList[i]] = pattern[i];
			else:
				if dict1[strList[i]] != pattern[i]:
					return False;
			
			if pattern[i] not in dict2:
				dict2[pattern[i]] = strList[i];
			else:
				if dict2[pattern[i]] != strList[i]:
					return False;
		
		return True;