class Solution(object):
	def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		
		if (not matrix):
			return 0
			
		rowNum = len(matrix); colNum = len(matrix[0]);
		result = [[0 for j in range(colNum)] for i in range(rowNum)];
		
		for i in range(0,rowNum):
			result[i][0] = int(matrix[i][0]);
		for j in range(0,colNum):
			result[0][j] = int(matrix[0][j]);
			
		for i in range (1,rowNum):
			for j in range(1,colNum):
				if (matrix[i][j] == '0'):
					result[i][j] = 0;
				else:
					result[i][j] = min(result[i-1][j-1],result[i][j-1],result[i-1][j])+1;
					
		maxSize = 0;
		for i in result:
			for j in i:
				if (j > maxSize):
					maxSize = j;
		return maxSize*maxSize;
	
a = ["0001","1101","1111","0111","0111"];
maximalSquare(a); 