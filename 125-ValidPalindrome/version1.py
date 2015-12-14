class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		
		if (len(s) <= 1):
			return True;
			
		letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
					's','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'];
					
		length = len(s);
		start = 0; end = length-1;
		while(start <= end):
			if (s[start].lower() not in letters):
				start += 1;
			if (s[end].lower() not in letters):
				end -= 1;
				
			if ((s[start].lower() in letters) and (s[end].lower() in letters)):
				
				if (s[start].lower() != s[end].lower()):
					return False;
				start += 1;
				end -= 1;
			
		return True;