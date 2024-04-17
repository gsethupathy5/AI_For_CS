# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isPossible(n, edges)
    print("\noutput:", serialize(ans, "boolean"))
