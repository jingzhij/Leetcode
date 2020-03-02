class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        meeting=[]
        heapq.heappush(meeting,intervals[0][1])
        for i in range(1,len(intervals)):
            if meeting[0]<=intervals[i][0]:
                heapq.heappop(meeting)
            heapq.heappush(meeting,intervals[i][1])
        return len(meeting)
