# Created by asetti2002 at 2024/04/25 20:36
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-performance-of-a-team/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        speed_sum, perf = 0, 0
        
        for eff, spd in engineers:
            heapq.heappush(heap, spd)
            speed_sum += spd
            
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            
            perf = max(perf, speed_sum * eff)
        
        return perf % mod
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    speed: List[int] = deserialize("List[int]", read_line())
    efficiency: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxPerformance(n, speed, efficiency, k)
    print("\noutput:", serialize(ans, "integer"))
