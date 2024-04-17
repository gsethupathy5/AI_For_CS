# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    src1: int = deserialize("int", read_line())
    src2: int = deserialize("int", read_line())
    dest: int = deserialize("int", read_line())
    ans = Solution().minimumWeight(n, edges, src1, src2, dest)
    print("\noutput:", serialize(ans, "long"))
