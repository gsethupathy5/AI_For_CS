# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/word-break-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    wordDict: List[str] = deserialize("List[str]", read_line())
    ans = Solution().wordBreak(s, wordDict)
    print("\noutput:", serialize(ans, "string[]"))
