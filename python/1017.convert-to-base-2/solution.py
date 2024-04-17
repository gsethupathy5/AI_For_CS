# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/convert-to-base-2/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def baseNeg2(self, n: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().baseNeg2(n)
    print("\noutput:", serialize(ans, "string"))
