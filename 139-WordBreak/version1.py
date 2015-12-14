class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: bool
		"""
		
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
		
s = Solution();
print s.wordBreak("leetcode",["lee", "code"]);