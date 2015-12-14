class Solution(object):
	
	def validElement(self, x, y, board):
		
		if board[x][y] != '.':
			temp = board[x][y];
			board[x][y] = '#';
			# check the same row
			for i in range(9):
				if temp == board[x][i]:
					return False;
				
			# check the same column
			for i in range(9):
				if temp == board[i][y]:
					return False;
					
			for i in range(3):
				for j in range(3):
					rowIndex = (x/3)*3 + i;
					columnIndex = (y/3)*3 + j;
					if temp == board[rowIndex][columnIndex]:
						return False;
			
			board[x][y] = temp;
			
		return True
	
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		
		for i in range(9):
			for j in range(9):
				if not self.validElement(i,j, board):
					return False
		
		return True;