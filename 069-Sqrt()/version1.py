class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		
		if (x==0):
			return x;
		
		left = 1; right = (x/2+1);
		while(left <= right):
			mid =  (left+right)/2;
			sqrt = mid*mid;
			sqrt2 = (mid+1)*(mid+1);
			if (x>=sqrt and x<sqrt2):
				return mid;
			elif (sqrt < x):
				left = mid +1;
			else:
				right = mid-1;
				
		return mid;
		