class Solution(object):
	
	def totalNQueens(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		
		def check(depth, indexList):
			'''
			:depth: the current row index 
			:indexList: the index of previous rows
			'''
			for i in range(0, depth):
				if (indexList[depth] == indexList[i]) or (abs(indexList[depth]-indexList[i]) == (depth-i)):
					return False;
			return True;
			
		def dfs(depth, indexList):
			if depth == n:
				result.append(indexList);
			else:
				# check every col index for row depth
				for i in range(0,n):
					indexList[depth] = i;
					if check(depth, indexList):
						dfs(depth+1, indexList);
		
		result = []
		indexList = [-1 for i in range(0,n)];
		dfs(0, indexList);
		return len(result);