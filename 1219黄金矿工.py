class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res=0
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        row,col=len(grid),len(grid[0])
        visited=[[False]*col for _ in range(row)]

        def dfs(x,y,gold):
            visited[x][y]=True
            self.res=max(self.res,gold)
            for i,j in directions:
                newX,newY=i+x,j+y
                if 0<=newX<row and 0<=newY<col and grid[newX][newY]!=0 and not visited[newX][newY]:
                    dfs(newX,newY,gold+grid[newX][newY])
            visited[x][y]=False #重置节点状态，改为未被探索

        for i in range(row):
            for j in range(col):
                if grid[i][j]!=0:
                    dfs(i,j,grid[i][j])
        return self.res

