class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		
		dict = {};
		for str in strs:
			temp = ''.join(sorted(str));
			
			if not temp in dict:
				dict[temp] = [str];
			else:
				dict[temp].append(str);
		
		result = dict.values();
		for i in range(len(result)):
			result[i].sort();
		
		return result;