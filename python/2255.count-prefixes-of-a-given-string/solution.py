# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-prefixes-of-a-given-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().countPrefixes(words, s)
    print("\noutput:", serialize(ans, "integer"))
