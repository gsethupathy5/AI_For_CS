# Created by asetti2002 at 2024/04/25 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-string-chain/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Your code here
        pass
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestStrChain(words)
    print("\noutput:", serialize(ans, "integer"))
