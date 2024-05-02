# Created by asetti2002 at 2024/05/01 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        return 0
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPairs(n, edges)
    print("\noutput:", serialize(ans, "long"))
