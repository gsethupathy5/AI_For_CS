# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minTrioDegree(n, edges)
    print("\noutput:", serialize(ans, "integer"))
