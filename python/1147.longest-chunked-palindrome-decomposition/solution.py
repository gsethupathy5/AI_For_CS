# Created by asetti2002 at 2024/04/25 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestDecomposition(self, text: str) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().longestDecomposition(text)
    print("\noutput:", serialize(ans, "integer"))
