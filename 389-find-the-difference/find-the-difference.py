class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        addedletters = ""
        freq = {}
        freq2 = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for j in t:
            if j in freq2:
                freq2[j] += 1
            else:
                freq2[j] = 1
        for  i in freq2:
            if i not in freq:
                return i
            elif freq2[i] > freq[i]:
                return i
            else:
                pass
            

       