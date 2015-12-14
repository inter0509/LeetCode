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
	
	def dfs(self, board, depth):
		'''
		:depth: int, indicate the position of '.' board element 
		'''
		if (depth == 81):
			return True;
		
		rowIndex = depth / 9;
		columnIndex = depth % 9;
		if (board[rowIndex][columnIndex] != '.'):
			return self.dfs(board,depth+1);
		else:
			for number in range(1,10):
				board[rowIndex][columnIndex] = str(number);
				if self.validElement(rowIndex, columnIndex, board) and self.dfs(board,depth+1):
					return True;
				board[rowIndex][columnIndex] = '.'
				
			return False;
			
		return True;
	
	
	def solveSudoku(self, board):
		# @param board, a 9x9 2D array
		# Solve the Sudoku by modifying the input board in-place.
		# Do not return any value.
		
		self.dfs(board, 0);