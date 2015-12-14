class Solution(object):
	
	def findKSmallest(self, nums1, nums2, K):
		'''
		: assuem that the first array is shorter than the second one
		'''
		
		len1 = len(nums1); len2 = len(nums2);
		if len1 > len2:
			return self.findKSmallest(nums2,nums1,K);
		if not len1:
			return nums2[K-1];
		if K == 1:
			return min(nums1[0],nums2[0]);
		
		index1 = min(K/2, len1);
		index2 = K - index1;
		
		if nums1[index1-1] == nums2[index2-1]:
			return nums1[index1-1];
		elif nums1[index1-1] > nums2[index2-1]: #the first k/2 part of nums2 cannot include the target element
			return self.findKSmallest(nums1, nums2[index2:],index1);
		else:
			return self.findKSmallest(nums1[index1:], nums2, index2);
	
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		
		sumLen = len(nums1)+len(nums2);
		if (sumLen%2) == 1:
			return self.findKSmallest(nums1, nums2, sumLen/2+1);
		else:
			return (self.findKSmallest(nums1, nums2, sumLen/2)+self.findKSmallest(nums1, nums2, sumLen/2+1))/2.0;