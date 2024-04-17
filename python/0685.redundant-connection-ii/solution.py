# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/redundant-connection-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findRedundantDirectedConnection(edges)
    print("\noutput:", serialize(ans, "integer[]"))
