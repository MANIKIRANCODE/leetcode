class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        reverse =0
        result =0
        total =0
        for index,character in enumerate(s):
            # print(i)
            result = ord(character) - ord('a') + 1
            # print(result)
            reverse = 27 - result 
            # print(reverse)
            total += (reverse * (index+1)) 
        return total