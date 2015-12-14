def getRow(rowIndex):
	"""
	:type rowIndex: int
	:rtype: List[int]
	"""
	
	result = [1]*(rowIndex+1);
	
	for i in range(0,rowIndex+1):
		for j in range(i-1,0,-1):
			result[j] = result[j]+result[j-1]
			
	return result;
	
print getRow(5);