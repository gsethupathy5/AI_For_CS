# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    distanceThreshold: int = deserialize("int", read_line())
    ans = Solution().findTheCity(n, edges, distanceThreshold)
    print("\noutput:", serialize(ans, "integer"))
