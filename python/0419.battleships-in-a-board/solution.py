# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/battleships-in-a-board/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().countBattleships(board)
    print("\noutput:", serialize(ans, "integer"))