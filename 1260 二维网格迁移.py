class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp=[]
        row,col=len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                temp.append(grid[i][j])
        n=len(temp)
        k=k%n   #对n取余数，移动n次相当于没移动，移动n+1次相当于移动1次，以此类推
        temp=temp[n-k:]+temp[:n-k]
        for i in range(row):
            for j in range(col):
                grid[i][j]=temp[i*col+j]    
        return grid
        
