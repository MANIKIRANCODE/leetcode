class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                distance = abs(freq[nums[i]]-i)
                if distance <= k:
                    print(distance)
                    return True
                else:
                    freq[nums[i]] = i
            else:
                freq[nums[i]] = i
        return False