# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/word-search-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findWords(board, words)
    print("\noutput:", serialize(ans, "string[]"))
