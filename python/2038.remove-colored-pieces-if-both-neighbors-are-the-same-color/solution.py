# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    colors: str = deserialize("str", read_line())
    ans = Solution().winnerOfGame(colors)
    print("\noutput:", serialize(ans, "boolean"))
