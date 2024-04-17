# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-possible-root-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    guesses: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().rootCount(edges, guesses, k)
    print("\noutput:", serialize(ans, "integer"))
