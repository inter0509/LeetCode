class Solution(object):
	def minimumTotal(self, triangle):
		
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		
		numRow = len(triangle);
		# DP: from bottom to top
		
		if (numRow == 1):
			return triangle[0][0];
		
		result = [];
		
		for i in range(numRow):
			result.append(triangle[numRow-1][i]);
		
		# dp[i][j] = triangle[i][j] + min(dp[i-1][j],dp[i-1][j+1]);
		for i in range(numRow-2,-1,-1):
			for j in range(0,i+1,1):
				result[j] = triangle[i][j]+min(result[j],result[j+1]);
				
		return result[0];