# Created by asetti2002 at 2024/04/25 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # code here
# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().maxRepOpt1(text)
    print("\noutput:", serialize(ans, "integer"))
