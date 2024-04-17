# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().longestBeautifulSubstring(word)
    print("\noutput:", serialize(ans, "integer"))
