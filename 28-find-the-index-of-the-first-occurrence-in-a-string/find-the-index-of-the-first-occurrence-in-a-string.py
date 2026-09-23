class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack = list(haystack)
        # needle = list(needle)
        # li =[]
        # count =0
        # for i in range(len(haystack)):
        #         for j in range(len(needle)):
        #                 if needle[j] == haystack[i]:
        #                         li.append(i)
                                
        #                         count+=1
        # if len(needle) == count:
        #     return li[0]
        # return -1
        for i in range(len(haystack)):
            result = haystack[i:i+len(needle)]
            if result == needle:
                return i
        else:
            return -1