# Created by asetti2002 at 2024/05/01 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-palindromic-subsequences/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countPalindromes(self, s: str) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countPalindromes(s)
    print("\noutput:", serialize(ans, "integer"))
