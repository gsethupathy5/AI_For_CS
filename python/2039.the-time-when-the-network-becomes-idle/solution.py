# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    patience: List[int] = deserialize("List[int]", read_line())
    ans = Solution().networkBecomesIdle(edges, patience)
    print("\noutput:", serialize(ans, "integer"))
