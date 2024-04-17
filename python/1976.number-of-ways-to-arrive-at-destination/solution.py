# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(n, roads)
    print("\noutput:", serialize(ans, "integer"))
