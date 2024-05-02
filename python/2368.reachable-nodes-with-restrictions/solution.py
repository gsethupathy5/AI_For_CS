# Created by asetti2002 at 2024/05/01 19:51
# leetgo: 1.4.3
# https://leetcode.com/problems/reachable-nodes-with-restrictions/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # Your code here
        pass
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    restricted: List[int] = deserialize("List[int]", read_line())
    ans = Solution().reachableNodes(n, edges, restricted)
    print("\noutput:", serialize(ans, "integer"))
