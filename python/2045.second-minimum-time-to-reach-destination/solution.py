# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    time: int = deserialize("int", read_line())
    change: int = deserialize("int", read_line())
    ans = Solution().secondMinimum(n, edges, time, change)
    print("\noutput:", serialize(ans, "integer"))
