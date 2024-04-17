# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximal-network-rank/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximalNetworkRank(n, roads)
    print("\noutput:", serialize(ans, "integer"))
