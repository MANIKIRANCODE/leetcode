from operator import itemgetter
class Solution:

    def frequencySort(self, s: str) -> str:
        freq = {}
        reverse = ""
        for i in s:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] =1
        sortedfrequency = dict(sorted(freq.items(),key=itemgetter(1),reverse = True))
        for i in sortedfrequency.items():
            reverse = reverse + i[0] * i[1]
        return reverse
            