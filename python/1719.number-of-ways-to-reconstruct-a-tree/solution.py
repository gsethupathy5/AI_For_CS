# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    pairs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkWays(pairs)
    print("\noutput:", serialize(ans, "integer"))
