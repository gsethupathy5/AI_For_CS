# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    connections: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().makeConnected(n, connections)
    print("\noutput:", serialize(ans, "integer"))
