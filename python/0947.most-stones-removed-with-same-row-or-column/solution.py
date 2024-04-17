# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    stones: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().removeStones(stones)
    print("\noutput:", serialize(ans, "integer"))
