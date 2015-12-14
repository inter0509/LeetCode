class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		
		dict = {};
		numberBullS = 0;
		numberCows = 0;
		
		for i in range(len(secret)):
			if secret[i] == guess[i]:
				numberBullS += 1;
			else:
				if secret[i] not in dict:
					dict[secret[i]] = 1;
				else:
					dict[secret[i]] += 1;
				
		for i in range(len(guess)):
			if guess[i] != secret[i]:
				if guess[i] in dict and dict[guess[i]] != 0:
					numberCows += 1;
					dict[guess[i]] -= 1
		
		return str(numberBullS)+'A'+str(numberCows)+'B';