# Created by asetti2002 at 2024/04/25 19:30
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shortestPathLength(graph)
    print("\noutput:", serialize(ans, "integer"))
