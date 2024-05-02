# Created by asetti2002 at 2024/04/25 20:31
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-palindromic-subsequences/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 if s != s[::-1] else 1
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removePalindromeSub(s)
    print("\noutput:", serialize(ans, "integer"))
