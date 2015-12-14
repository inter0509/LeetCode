class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		
		length = len(prices);
		if length==0 or length==1:
			return 0;
		# profit1[i] is the max profit in prices[:i]
		profit1 = [0 for i in range(length)];
		# profit1[i] is the max profit in prices[i:]
		profit2 = [0 for i in range(length)];
		profit1[0] = 0;
		profit2[length-1] = 0;
		
		minPrice = prices[0];
		for i in range(1,length):
			if prices[i] < minPrice:
				minPrice = prices[i];
			profit1[i] = max(profit1[i-1], prices[i]-minPrice);
			
		maxPrice = prices[length-1];
		for i in range(length-2,-1,-1):
			if prices[i] > maxPrice:
				maxPrice = prices[i];
			profit2[i] = max(profit2[i+1], maxPrice-prices[i]);
		
		maxGain = 0;
		for i in range(length):
			maxGain = max(maxGain, profit1[i]+profit2[i]);
			
		return maxGain;