class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentelement = 0
        maximum =nums[0]
        previoussum =0
        for i in range(len(nums)):
            currentelement = nums[i]
            previoussum += currentelement
            maximum = max(previoussum,maximum)
            if previoussum < 0:
                previoussum  = 0
        return maximum
    
        