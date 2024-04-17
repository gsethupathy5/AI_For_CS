# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    hasApple: List[bool] = deserialize("List[bool]", read_line())
    ans = Solution().minTime(n, edges, hasApple)
    print("\noutput:", serialize(ans, "integer"))
