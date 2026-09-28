class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        index = []
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        sorted_array =sorted(freq.items(),key = lambda x:x[1],reverse = True)
      
        sorted_array = sorted_array[:k]
        for i in range(len(sorted_array)):
            index.append(sorted_array[i][0])
        return index