# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/count-servers-that-communicate/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countServers(grid)
    print("\noutput:", serialize(ans, "integer"))
