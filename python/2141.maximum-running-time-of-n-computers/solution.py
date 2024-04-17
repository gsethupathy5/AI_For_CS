# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-running-time-of-n-computers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    batteries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxRunTime(n, batteries)
    print("\noutput:", serialize(ans, "long"))
