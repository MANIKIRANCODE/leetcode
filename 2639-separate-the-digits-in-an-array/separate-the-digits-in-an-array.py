class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = list(map(str,nums))
        result = "".join(nums)
        var = list(result)
        var = list(map(int,var))
        return var
