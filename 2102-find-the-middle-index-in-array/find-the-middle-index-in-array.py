class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = 0
        for i in nums:
            totalsum += i
        leftsum =0
        for i in range(len(nums)):
            rightsum = totalsum - leftsum - nums[i]
            if(leftsum == rightsum):
                return i
            leftsum += nums[i]
        return -1
            