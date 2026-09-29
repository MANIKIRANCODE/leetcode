class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for i in range(0,len(nums)):
            current = nums[i]
            compliment = target - current 
            if compliment in hashtable:
                return [hashtable[compliment],i]
            else:
                hashtable[nums[i]] = i
