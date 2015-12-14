class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		
		added = 1;
		
		for i in range(len(digits)-1,-1,-1):
			sum = added + digits[i];
			digits[i] = sum % 10;
			added = sum / 10;
			print added
			
		if added != 0:
			digits.insert(0, added);
			
		return digits;