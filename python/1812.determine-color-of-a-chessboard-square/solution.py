# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    coordinates: str = deserialize("str", read_line())
    ans = Solution().squareIsWhite(coordinates)
    print("\noutput:", serialize(ans, "boolean"))
