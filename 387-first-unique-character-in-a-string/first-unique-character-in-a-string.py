class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = list(s)
        freq = {}
        for i in letters:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] =1
        for i in range(0,len(letters)):
            if freq[letters[i]] == 1:
                return i
        return -1