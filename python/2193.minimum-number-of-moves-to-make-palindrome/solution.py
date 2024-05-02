# Created by asetti2002 at 2024/04/25 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        moves = 0
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                moves += 1
        
        return moves
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minMovesToMakePalindrome(s)
    print("\noutput:", serialize(ans, "integer"))
