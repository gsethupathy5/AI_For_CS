# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/merge-strings-alternately/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().mergeAlternately(word1, word2)
    print("\noutput:", serialize(ans, "string"))
