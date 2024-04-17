# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/bus-routes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    routes: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numBusesToDestination(routes, source, target)
    print("\noutput:", serialize(ans, "integer"))
