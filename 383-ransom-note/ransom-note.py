class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomfrequency = {}
        magazinefrequency = {}
        for i in ransomNote:
            if i in ransomfrequency:
                ransomfrequency[i] += 1
            else:
                ransomfrequency[i] = 1

        for j in magazine:
            if j in magazinefrequency:
                magazinefrequency[j] += 1
            else:
                magazinefrequency[j] = 1
            
        for i in ransomfrequency:
            if i not in magazinefrequency:
                    return False
            else:pass
            if magazinefrequency[i] < ransomfrequency[i]:
                    return False
            else:
                    pass
            
        return True
                  
                    
 