class Solution(object):
	def findKthLargest(self, array, k):
		"""
		:type array: List[int]
		:type k: int
		:rtype: int
		"""
		
		def partition(array, left, right):
			
			# pick the last element as the pivot
			pivotVal = array[right];
			i = left;
			
			# from left to right-1
			for j in range(left,right):
				if array[j] > pivotVal:
					# put large values in the left part
					array[j],array[i] = array[i],array[j];
					i += 1;
					
			array[i],array[right] = array[right],array[i]
			
			return i;
		
		def findKthLargestWithBound(array, k, left, right):
			partitionIndex = partition(array,left,right);
			if partitionIndex == k-1:
				return array[partitionIndex];
			elif partitionIndex >= k:
				return findKthLargestWithBound(array, k, left, partitionIndex-1);
			else:
				return findKthLargestWithBound(array, k, partitionIndex+1, right);
				
		return findKthLargestWithBound(array, k, 0, len(array)-1);
		
s = Solution();
print s.findKthLargest([3,2,1,5,6,4],1);