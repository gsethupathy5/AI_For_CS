# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/decode-ways/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numDecodings(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numDecodings(s)
    print("\noutput:", serialize(ans, "integer"))
