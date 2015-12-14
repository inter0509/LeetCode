class Solution(object):
	
	def dfs(self, x, y, board, word):
		'''
		: dfs starting from (x,y);
		'''
		
		if not word:
			return True;
		
		if x > 0 and board[x-1][y] == word[0]:
			temp = board[x][y]; board[x][y] = '#';
			if (self.dfs(x-1, y, board, word[1:])):
				return True;
			board[x][y] = temp;
			
		if y > 0 and board[x][y-1] == word[0]:
			temp = board[x][y]; board[x][y] = '#';
			if (self.dfs(x, y-1, board, word[1:])):
				return True;
			board[x][y] = temp;
		
		if x < (len(board)-1) and board[x+1][y] == word[0]:
			temp = board[x][y]; board[x][y] = '#';
			if (self.dfs(x+1, y, board, word[1:])):
				return True;
			board[x][y] = temp;
		
		if y < (len(board[0])-1) and board[x][y+1] == word[0]:
			temp = board[x][y]; board[x][y] = '#';
			if (self.dfs(x, y+1, board, word[1:])):
				return True;
			board[x][y] = temp;
			
		return False;
	
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		
		if not word:
			return True;
		if not board:
			return False;
			
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == word[0]:
					if self.dfs(i,j,board,word[1:]):
						return True;
		
		return False;
		