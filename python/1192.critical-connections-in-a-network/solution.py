# Created by asetti2002 at 2024/04/25 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/critical-connections-in-a-network/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        pass
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    connections: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().criticalConnections(n, connections)
    print("\noutput:", serialize(ans, "integer[][]"))
