class NumMatrix(object):
	def __init__(self, matrix):
		"""
		initialize your data structure here.
		:type matrix: List[List[int]]
		"""
		
		if not matrix:
			return;
		
		rowLen = len(matrix);
		colLen = len(matrix[0]);
		
		self.dis = [[0 for i in range(colLen+1)] for j in range(rowLen+1)];
		for i in range(rowLen):
			for j in range(colLen):
				self.dis[i+1][j+1] = self.dis[i+1][j]+self.dis[i][j+1]+matrix[i][j]-self.dis[i][j];
				
	
	def sumRegion(self, row1, col1, row2, col2):
		"""
		sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
		:type row1: int
		:type col1: int
		:type row2: int
		:type col2: int
		:rtype: int
		"""
		
		return self.dis[row2+1][col2+1]-self.dis[row1][col2+1]-self.dis[row2+1][col1]+self.dis[row1][col1]
	
	
# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)