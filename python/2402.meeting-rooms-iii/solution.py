# Created by asetti2002 at 2024/05/01 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/meeting-rooms-iii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        import heapq
        
        meetings.sort()
        heap = []
        rooms = [[] for _ in range(n)]
        
        for m in meetings:
            start = m[0]
            for i in range(len(rooms)):
                if not rooms[i] or heapq.heappop(rooms[i]) <= start:
                    heapq.heappush(rooms[i], m[1])
                    break
        
        max_meetings = 0
        room_number = 0
        
        for i in range(len(rooms)):
            if len(rooms[i]) > max_meetings:
                max_meetings = len(rooms[i])
                room_number = i
        
        return room_number
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    meetings: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().mostBooked(n, meetings)
    print("\noutput:", serialize(ans, "integer"))
