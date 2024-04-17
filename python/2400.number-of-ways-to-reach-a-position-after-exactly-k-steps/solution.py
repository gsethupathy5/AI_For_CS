# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    startPos: int = deserialize("int", read_line())
    endPos: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfWays(startPos, endPos, k)
    print("\noutput:", serialize(ans, "integer"))
