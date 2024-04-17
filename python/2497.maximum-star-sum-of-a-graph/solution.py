# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    vals: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxStarSum(vals, edges, k)
    print("\noutput:", serialize(ans, "integer"))
