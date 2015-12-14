class Solution(object):
	
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		
		def convertToString(indexList):
			dot = ''.join(['.']*n);
			dotVect = [dot for i in range(n)];
			for i in range(n):
				temp = list(dotVect[i]);
				temp[indexList[i]] = 'Q';
				dotVect[i] = ''.join(temp);
				
			result.append(dotVect);
		
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
				convertToString(indexList);
			else:
				# check every col index for row depth
				for i in range(0,n):
					indexList[depth] = i;
					if check(depth, indexList):
						dfs(depth+1, indexList);
		
		result = [];
		indexList = [-1 for i in range(0,n)];
		dfs(0, indexList);
		return result;