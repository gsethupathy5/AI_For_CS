# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/determine-if-two-strings-are-close/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().closeStrings(word1, word2)
    print("\noutput:", serialize(ans, "boolean"))
