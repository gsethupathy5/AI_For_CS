# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    hats: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberWays(hats)
    print("\noutput:", serialize(ans, "integer"))
