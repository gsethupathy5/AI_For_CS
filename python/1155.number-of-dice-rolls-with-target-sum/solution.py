# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numRollsToTarget(n, k, target)
    print("\noutput:", serialize(ans, "integer"))
