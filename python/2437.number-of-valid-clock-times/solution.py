# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-valid-clock-times/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countTime(self, time: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    time: str = deserialize("str", read_line())
    ans = Solution().countTime(time)
    print("\noutput:", serialize(ans, "integer"))
