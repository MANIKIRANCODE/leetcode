class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        nums.sort()
        for i in range(0,len(nums),2):
            current = nums[i]
            adjacent = nums[i+1]
            total += min(current,adjacent)
        return total