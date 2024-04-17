# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    darts: List[List[int]] = deserialize("List[List[int]]", read_line())
    r: int = deserialize("int", read_line())
    ans = Solution().numPoints(darts, r)
    print("\noutput:", serialize(ans, "integer"))
