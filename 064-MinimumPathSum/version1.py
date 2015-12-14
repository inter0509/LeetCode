class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
	
		rowNum = len(grid); colNum = len(grid[0]);
		result = [[0 for j in range(colNum)] for i in range(rowNum)];
		result[0][0] = grid[0][0];
		
		
		for i in range(1,rowNum):
			result[i][0] = result[i-1][0]+grid[i][0];
		for j in range(1,colNum):
			result[0][j] = result[0][j-1]+grid[0][j];
		
		for i in range(1,rowNum):
			for j in range(1,colNum):
				result[i][j] = min(result[i-1][j],result[i][j-1])+grid[i][j];
			
		for i in result:
			print i;
			
		return result[rowNum-1][colNum-1];