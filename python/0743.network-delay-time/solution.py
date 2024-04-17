# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/network-delay-time/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    times: List[List[int]] = deserialize("List[List[int]]", read_line())
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().networkDelayTime(times, n, k)
    print("\noutput:", serialize(ans, "integer"))
