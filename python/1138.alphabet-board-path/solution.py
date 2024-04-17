# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/alphabet-board-path/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    target: str = deserialize("str", read_line())
    ans = Solution().alphabetBoardPath(target)
    print("\noutput:", serialize(ans, "string"))
