class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        left = 0
        right = 0
        answer = [ ]
        for i in nums:
            total += i
            # print(total)
        for i in range(len(nums)):
        
        # print(left)
            right = total - nums[i] - left
        # print(right)
            answer.append(abs(left - right))
            left += nums[i]
        return  answer