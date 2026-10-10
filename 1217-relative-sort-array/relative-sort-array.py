class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        remaining = []
        result = []
        for i in arr1:
            if i not in arr2:
                remaining.append(i)
        freq ={}
        for i in arr1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for  i in arr2:
            if i in arr1:
                for x in range(freq[i]):
                    result.append(i)
            else:pass
        remaining.sort()
        result.extend(remaining)
        return result