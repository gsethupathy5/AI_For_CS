# Created by asetti2002 at 2024/05/01 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-good-paths/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # implementation of the solution
        pass
# @lc code=end

if __name__ == "__main__":
    vals: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberOfGoodPaths(vals, edges)
    print("\noutput:", serialize(ans, "integer"))
