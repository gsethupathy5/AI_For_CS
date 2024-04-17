# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/odd-string-difference/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def oddString(self, words: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().oddString(words)
    print("\noutput:", serialize(ans, "string"))
