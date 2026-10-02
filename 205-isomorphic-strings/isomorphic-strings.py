class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping_s = {}
        mapping_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            if char1 in mapping_s :
                if mapping_s[char1] != char2:
                    return False

            else:
               mapping_s[char1] = char2
            
            if char2 in mapping_t :
                if mapping_t[char2] != char1:
                    return False

            else:
               mapping_t[char2] = char1

            
        return True




            

