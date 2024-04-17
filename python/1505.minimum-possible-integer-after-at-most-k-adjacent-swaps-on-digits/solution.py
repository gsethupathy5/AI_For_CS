# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minInteger(num, k)
    print("\noutput:", serialize(ans, "string"))
