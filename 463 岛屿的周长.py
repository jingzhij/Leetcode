思路：因为周长是对称的，所以求出上方和左方 *2就是结果 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,col= len(grid),len(grid[0])
        s=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0: s+=1
                    if j==0 or grid[i][j-1]==0: s+=1
        return s*2
