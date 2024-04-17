# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    steps: int = deserialize("int", read_line())
    arrLen: int = deserialize("int", read_line())
    ans = Solution().numWays(steps, arrLen)
    print("\noutput:", serialize(ans, "integer"))
