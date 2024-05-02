# Created by asetti2002 at 2024/04/25 20:39
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        num = int(s, 2)
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            res += 1
        return res
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numSteps(s)
    print("\noutput:", serialize(ans, "integer"))
