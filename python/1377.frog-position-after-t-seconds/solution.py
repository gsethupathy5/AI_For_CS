# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/frog-position-after-t-seconds/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    t: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().frogPosition(n, edges, t, target)
    print("\noutput:", serialize(ans, "double"))
