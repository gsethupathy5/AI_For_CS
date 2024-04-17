# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    pref: str = deserialize("str", read_line())
    ans = Solution().prefixCount(words, pref)
    print("\noutput:", serialize(ans, "integer"))
