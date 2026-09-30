class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        duplicates = {}
        for i in range(len(nums)):
            if nums[i] in duplicates:
                distance = abs(duplicates[nums[i]]-i)
                if distance <= k:
                    return True
                else:
                    duplicates[nums[i]] = i
            else:
                duplicates[nums[i]] = i
        return False