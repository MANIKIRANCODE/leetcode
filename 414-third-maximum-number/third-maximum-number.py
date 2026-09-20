class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thirdest = None
        secondest = None
        first =None
        result = 0
        duplicate = []
        for i in range(0,len(nums)):
            if nums[i] not in duplicate:
                duplicate.append(nums[i])

                if (nums[i] > first):
                    thirdest = secondest
                    secondest = first
                    first = nums[i]
           
                elif nums[i] > secondest  and first > nums[i]:
                    thirdest = secondest
                    secondest = nums[i]
                elif nums[i] > thirdest and first > nums[i] and secondest > nums[i]:
                    thirdest = nums[i]
            else:
                pass

        if len(duplicate) < 3:
            return first
        else:
            return thirdest

     
                

                
        