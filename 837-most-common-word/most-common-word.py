import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        maximum = 0
        freq = {}
        paragraph = paragraph.lower()
        for i in string.punctuation:
            paragraph = paragraph.replace(i," ")
        paragraph = paragraph.split()
        for i in paragraph:
                if i in freq:
                    freq[i] +=1
                else:
                    freq[i] = 1
        for i in freq:
            if freq[i] > maximum  and i not in banned:
                maximum = freq[i]
                ans = i
        return ans
        

                
