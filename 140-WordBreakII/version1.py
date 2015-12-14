class Solution(object):
	def validBroken(self, s, wordDict):
		
		length = len(s);
		vect = [False for i in range(length+1)];
		
		vect[0] = True;
		
		# vect[i] indicates if the first i substring of s can be broken or not
		for i in range(1, length+1):
			for j in range(0, i):
				subStr = s[j:i];
				if vect[j] and subStr in wordDict:
					vect[i] = True;
					break;
					
		return vect[length];
		
	def dfs(self, s, wordDict, current, results):
		if self.validBroken(s,wordDict):
			if not s:
				results.append(''+current);
		
			for i in range(1,len(s)+1):
				if s[:i] in wordDict:
					if current:
						self.dfs(s[i:], wordDict, current+' '+s[:i], results);
					else:
						self.dfs(s[i:], wordDict, current+s[:i], results);
					
					
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: List[str]
		"""
		
		results = [];
		self.dfs(s, wordDict, '', results);
		return results;