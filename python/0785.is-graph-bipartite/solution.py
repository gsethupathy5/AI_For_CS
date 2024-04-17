# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/is-graph-bipartite/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isBipartite(graph)
    print("\noutput:", serialize(ans, "boolean"))
