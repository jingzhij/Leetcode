题解：求最大公约数
设x，y的最大公约数为m，z如果是m整数倍，那么一定可以
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z==0:
            return True
        if x+y<z:
            return False
        if x==0:
            return y==z
        if x>y:
            y,x=x,y
        while y%x!=0:
            y,x=x,y%x
        return z%x==0 
        

