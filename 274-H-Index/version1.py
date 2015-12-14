class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		
		'''
		* An example
		*  nums  : 0  3  3  3  6  7  9 
		* -----------------table---------------------
		*       n     : 0  1  2  3  4  5  6  >=7  (length = 7) 
		* appearance  : 0  0  0  3  0  0  1   2
		* -------------------------------------------
		'''
		
		length = len(citations);
		vect = [0 for i in range(length+1)];
		
		for citation in citations:
			if citation >= length:
				vect[length] += 1;
			else:
				vect[citation] += 1;
		
		sumCitation = 0;
		for i in range(length, -1, -1):
			sumCitation += vect[i];
			if sumCitation >= i:
				return i;
				
		return 0;