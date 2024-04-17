# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-path-quality-of-a-graph/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    maxTime: int = deserialize("int", read_line())
    ans = Solution().maximalPathQuality(values, edges, maxTime)
    print("\noutput:", serialize(ans, "integer"))
