from heapq import heapify,heappop,heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapify(stones)
        while len(stones)>0:
            y=-heappop(stones)
            if len(stones)==0:
                return y
            x=-heappop(stones)
            heappush(stones,x-y)
    
            
