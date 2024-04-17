# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().countVowelSubstrings(word)
    print("\noutput:", serialize(ans, "integer"))
