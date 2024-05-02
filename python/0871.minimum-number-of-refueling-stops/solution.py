# Created by asetti2002 at 2024/04/25 19:33
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-refueling-stops/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        import heapq
        
        pq = [] 
        stations.append((target, 0))
        
        res = prev = 0
        tank = startFuel
        
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:
                tank += -heapq.heappop(pq)
                res += 1
            if tank < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location
            
        return res
# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    startFuel: int = deserialize("int", read_line())
    stations: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minRefuelStops(target, startFuel, stations)
    print("\noutput:", serialize(ans, "integer"))
