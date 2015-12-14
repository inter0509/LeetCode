class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		
		
		RowNum = len(obstacleGrid); ColNum = len(obstacleGrid[0]);
		matrix = [[0 for j in range(ColNum)] for i in range(RowNum)];
		
		for i in range(RowNum):
			if (obstacleGrid[i][0] == 0):
				matrix[i][0] = 1;
			else:
				break;
				
		for j in range(ColNum):
			if (obstacleGrid[0][j] == 0):
				matrix[0][j] = 1;
			else:
				break;
				
		for i in range(1,RowNum):
			for j in range(1,ColNum):
				if (obstacleGrid[i][j] == 1):
					matrix[i][j] = 0;
				else:
					matrix[i][j] = matrix[i-1][j]+matrix[i][j-1];
					
		return matrix[RowNum-1][ColNum-1];