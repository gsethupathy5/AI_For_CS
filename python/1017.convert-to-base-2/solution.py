# Created by asetti2002 at 2024/04/25 19:54
# leetgo: 1.4.3
# https://leetcode.com/problems/convert-to-base-2/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0: return "0"
        res = ""
        while n != 0:
            res = str(n & 1) + res
            n = -(n >> 1)
        return res
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().baseNeg2(n)
    print("\noutput:", serialize(ans, "string"))
