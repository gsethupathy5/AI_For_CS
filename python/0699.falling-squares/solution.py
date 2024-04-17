# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/falling-squares/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    positions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().fallingSquares(positions)
    print("\noutput:", serialize(ans, "integer[]"))
