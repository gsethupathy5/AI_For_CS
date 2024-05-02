# Created by asetti2002 at 2024/05/01 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxPalindromes(s, k)
    print("\noutput:", serialize(ans, "integer"))
