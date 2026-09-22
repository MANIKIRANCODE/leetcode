class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isvowels(st):
            vowels = {"a","e","i","o","u","A","E","I","O","U"}
            return st in vowels 
        left = 0
        temp=0
        s = list(s)
        right = len(s) -1
        while(left < right):
            while left<right and not isvowels(s[left]):
              left +=1
            while left<right and not isvowels(s[right]):
               right -= 1
            if left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -=1
        return "".join(s)