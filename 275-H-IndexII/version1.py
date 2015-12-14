class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		
		# binary sesearch
		
		length = len(citations);
		left = 0; right = length-1;
		while left <= right:
			mid = (left+right)/2;
			# very few highly-cited papers 
			if (citations[mid]+mid>=length):
				right = mid-1;
			# most are highly-cited papers
			else:
				left = mid + 1;
				
		return length-left;