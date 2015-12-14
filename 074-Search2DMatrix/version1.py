class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		
		if (len(matrix) == 0):
			return False;
		
		rowIndex = 0;
		columnIndex = len(matrix[0])-1;
		
		while((rowIndex<len(matrix)) and (columnIndex >= 0)):
			if (target > matrix[rowIndex][columnIndex]):
				rowIndex += 1;
			elif (target < matrix[rowIndex][columnIndex]):
				columnIndex -= 1;
			else:
				return True;
			
		return False;