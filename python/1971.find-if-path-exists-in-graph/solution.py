# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    destination: int = deserialize("int", read_line())
    ans = Solution().validPath(n, edges, source, destination)
    print("\noutput:", serialize(ans, "boolean"))
