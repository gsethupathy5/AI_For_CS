# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/node-with-highest-edge-score/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    edges: List[int] = deserialize("List[int]", read_line())
    ans = Solution().edgeScore(edges)
    print("\noutput:", serialize(ans, "integer"))
