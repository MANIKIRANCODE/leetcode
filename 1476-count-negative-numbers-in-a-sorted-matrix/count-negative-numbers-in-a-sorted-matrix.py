class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] < 0:
                    count+=1
                else:
                    pass
        return count
                 