class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums);
        pointer = length - 1;
        i = 0;
        NumOfInstan = 0;

        while(i <= pointer):
            if (nums[i] == val):
                nums[i] = nums[pointer];
                pointer -= 1;
                NumOfInstan += 1;
            else:
                i += 1;

        return (length-NumOfInstan);