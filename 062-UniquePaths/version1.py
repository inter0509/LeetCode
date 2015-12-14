class Solution(object):
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		
		matrix = [];
		if (m==1 and n==1):
			return 1;
		elif (m==1 and n!=1):
			return 1;
		elif (m!=1 and n==1):
			return 1;
		else:
			matrix = [[0 for j in range(n)] for i in range(m)];
			for j in range(1,n):
				matrix[0][j] = 1;
			for i in range(1,m):
				matrix[i][0] = 1;
			for i in range(1,m):
				for j in range(1,n):
					matrix[i][j] = matrix[i][j-1]+matrix[i-1][j];
					
		return matrix[m-1][n-1];