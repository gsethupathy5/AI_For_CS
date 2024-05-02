# Created by asetti2002 at 2024/04/25 19:35
# leetgo: 1.4.3
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Your code here
        pass
# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    maxMoves: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().reachableNodes(edges, maxMoves, n)
    print("\noutput:", serialize(ans, "integer"))
