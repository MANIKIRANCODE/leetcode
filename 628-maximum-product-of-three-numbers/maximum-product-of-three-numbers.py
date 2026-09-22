class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
       #finding the largest first and secondest and thirdest element from the array
        
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        firstsmall = float("+inf")
        secondsmall = float("+inf")

        for i in nums:
            if i >= first:
                third = second
                second=first
                first = i
            elif  i >= second and i <= first:
                third = second
                second = i
            elif i >= third and i <= second:
                third = i
            else:
                pass
           
        for j in nums:
            if j <= firstsmall:
                
                secondsmall=firstsmall
                firstsmall = j
            elif  j <= secondsmall  and j >= firstsmall :
                
                secondsmall  = j
            else:
                pass     
        largest = first * second * third
        smallest = firstsmall * secondsmall * first
        return max(largest,smallest)
