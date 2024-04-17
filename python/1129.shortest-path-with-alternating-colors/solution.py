# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-path-with-alternating-colors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    redEdges: List[List[int]] = deserialize("List[List[int]]", read_line())
    blueEdges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shortestAlternatingPaths(n, redEdges, blueEdges)
    print("\noutput:", serialize(ans, "integer[]"))
