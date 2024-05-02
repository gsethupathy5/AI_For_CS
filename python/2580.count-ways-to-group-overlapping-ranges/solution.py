# Created by asetti2002 at 2024/05/01 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    ranges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countWays(ranges)
    print("\noutput:", serialize(ans, "integer"))
