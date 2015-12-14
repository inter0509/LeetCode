class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		
		if not prices:
			return 0;
		
		maxGain = 0;
		for i in range(1,len(prices)):
			if prices[i]>prices[i-1]:
				maxGain += (prices[i]-prices[i-1]);
				
		return maxGain;