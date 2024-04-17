# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minMovesToMakePalindrome(s)
    print("\noutput:", serialize(ans, "integer"))
