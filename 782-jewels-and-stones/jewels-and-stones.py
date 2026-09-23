class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        stones = list(stones) 
        jewels = list(jewels)
        count = 0
        for i in range(0,len(jewels)):
            for j in stones:
                if jewels[i] == j:
                    count+=1
        return count
        