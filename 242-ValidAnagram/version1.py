class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		
		l1 = len(s); l2 = len(t);
		if not l1 ==  l2:
			return False;
		if (l1==0 and l2==0):
			return True;
		
		dict = {}
		for i in range(len(s)):
			if s[i] in dict:
				dict[s[i]] += 1;
			else:
				dict[s[i]] = 1;
		
		for i in range(len(s)):
			if t[i] in dict:
				dict[t[i]] -= 1;
			else:
				return False
		
		for key in dict:
			if dict[key] != 0:
				return False;
				
		return True;