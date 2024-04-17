# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/word-ladder-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    beginWord: str = deserialize("str", read_line())
    endWord: str = deserialize("str", read_line())
    wordList: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findLadders(beginWord, endWord, wordList)
    print("\noutput:", serialize(ans, "string[][]"))
