class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		
		
		
		len1 = len(word1);
		len2 = len(word2);
		
		mat = [None]*(len1+1);
		for i in range(0,len1+1):
			mat[i] = [None]*(len2+1);
		
		mat[0][0] = 0;
		for i in range(1,len1+1):
			mat[i][0] = i;
		for j in range(1,len2+1):
			mat[0][j] = j;
		
		for i in range(1,len1+1):
			for j in range(1,len2+1):
				if (word1[i-1] == word2[j-1]):
					mat[i][j] = mat[i-1][j-1]; #substitution
				else:
					mat[i][j] = min(mat[i-1][j-1]+1,mat[i][j-1]+1,mat[i-1][j]+1);
		
		return mat[len1][len2];