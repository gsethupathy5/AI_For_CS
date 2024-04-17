# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    flips: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numTimesAllBlue(flips)
    print("\noutput:", serialize(ans, "integer"))
