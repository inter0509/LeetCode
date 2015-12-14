class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		
		result = [None]*numRows;
		
		for i in range(numRows):
			result[i] = [0]*(i+1);
			result[i][0] = 1;
			result[i][i] = 1;
			
			for j in range(1,i):
				result[i][j] = result[i-1][j-1]+result[i-1][j];
	
		return result;