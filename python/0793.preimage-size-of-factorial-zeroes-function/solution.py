# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    ans = Solution().preimageSizeFZF(k)
    print("\noutput:", serialize(ans, "integer"))
