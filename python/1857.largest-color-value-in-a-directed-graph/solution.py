# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

# @lc code=end

if __name__ == "__main__":
    colors: str = deserialize("str", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestPathValue(colors, edges)
    print("\noutput:", serialize(ans, "integer"))
