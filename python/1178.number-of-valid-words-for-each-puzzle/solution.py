# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    puzzles: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findNumOfValidWords(words, puzzles)
    print("\noutput:", serialize(ans, "integer[]"))
