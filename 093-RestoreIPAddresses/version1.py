class Solution(object):
	
	
	
	def dfs(self, s, count, current, results):
		
		def validString(string):
			if not string:
				return False;
			
			stringInt = int(string);
			
			# deal with str like '010'
			if string[0] == '0':
				return (string=='0');
			
			if stringInt<=255 and stringInt>=0:
				return True;
			return False;
		
		if count == 3 and validString(s):
			results.append(''+current+s);
			return;
			
		for i in range(1,4):
			temp = s[:i];
			#temp2 = current;
			#current += current+'.'+str(temp);
			if validString(temp):
				self.dfs(s[i:], count+1, current+str(temp)+'.', results);
			#current = temp2;
	
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		
		results = [];
		length = len(s);
		if length<4 or length>12:
			return results;
		
		self.dfs(s, 0, '', results);
		return results;