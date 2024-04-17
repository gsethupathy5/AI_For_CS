# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/find-eventual-safe-states/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().eventualSafeNodes(graph)
    print("\noutput:", serialize(ans, "integer[]"))
