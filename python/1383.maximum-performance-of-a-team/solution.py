# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-performance-of-a-team/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    speed: List[int] = deserialize("List[int]", read_line())
    efficiency: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxPerformance(n, speed, efficiency, k)
    print("\noutput:", serialize(ans, "integer"))
