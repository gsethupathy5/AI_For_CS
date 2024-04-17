# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().firstPalindrome(words)
    print("\noutput:", serialize(ans, "string"))
