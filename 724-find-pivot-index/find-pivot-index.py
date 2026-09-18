class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftside = 0
        rightside =sum(nums)
        for i in range(len(nums)):
            rightside -= nums[i]
            if leftside == rightside:
                return i
            else:
                leftside += nums[i]
           
                
        return -1 