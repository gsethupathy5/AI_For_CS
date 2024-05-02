# Created by asetti2002 at 2024/04/25 19:30
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-distance-to-closest-person/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        n = len(seats)
        prev = None
        
        for i, seat in enumerate(seats):
            if seat == 1:
                if prev is None:
                    max_dist = i
                else:
                    max_dist = max(max_dist, (i - prev) // 2)
                prev = i
                
        max_dist = max(max_dist, n - 1 - prev)
        
        return max_dist
# @lc code=end

if __name__ == "__main__":
    seats: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxDistToClosest(seats)
    print("\noutput:", serialize(ans, "integer"))
