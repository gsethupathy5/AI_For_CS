# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    connections: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minReorder(n, connections)
    print("\noutput:", serialize(ans, "integer"))
