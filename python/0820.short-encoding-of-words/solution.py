# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/short-encoding-of-words/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minimumLengthEncoding(words)
    print("\noutput:", serialize(ans, "integer"))
