class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		
		# find max(prices[i]-prices[j] for j < i);
		
		if not prices:
			return 0;
		
		maxGain = 0;
		lowPrice = prices[0];
		
		for i in range(1,len(prices)):
			if prices[i] < lowPrice:
				lowPrice = prices[i];
			maxGain = max(maxGain, prices[i]-lowPrice);
				
		return maxGain