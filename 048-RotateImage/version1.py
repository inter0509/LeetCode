class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		
		siz = len(matrix);
		for i in range(0,siz):
			for j in range(i+1,siz):
				matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j];
				
		for i in range(0,siz):
			matrix[i].reverse();