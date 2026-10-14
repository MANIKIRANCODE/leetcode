class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
      
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        frequency = {}

        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        sortedfreq = dict(sorted(frequency.items(),key=lambda item:(-item[1],item[0])))
        wordfre = list(sortedfreq.keys())
        return wordfre[0:k]
