class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = list(s)
        left = 0
        right = len(words)-1
        while(left<right):
            if words[left].isalpha() and words[right].isalpha():
                temp = words[left]
                words[left] = words[right]
                words[right] = temp
                left += 1
                right -= 1
            elif not words[left].isalpha():
                left+=1
            elif not words[right].isalpha():
                right -=1
        return "".join(words)