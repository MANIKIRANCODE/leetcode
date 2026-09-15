class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = s.lower()
        ls = []
        for i  in low:
            if i.isalnum():
                ls.append(i)
        string = "".join(ls)
        return string == string[::-1]
                 
        