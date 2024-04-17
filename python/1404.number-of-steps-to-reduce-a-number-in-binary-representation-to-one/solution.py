# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numSteps(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numSteps(s)
    print("\noutput:", serialize(ans, "integer"))
