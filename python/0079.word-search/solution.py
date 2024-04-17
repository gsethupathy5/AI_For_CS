# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/word-search/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    word: str = deserialize("str", read_line())
    ans = Solution().exist(board, word)
    print("\noutput:", serialize(ans, "boolean"))
