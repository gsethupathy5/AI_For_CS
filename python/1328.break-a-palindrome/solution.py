# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/break-a-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    palindrome: str = deserialize("str", read_line())
    ans = Solution().breakPalindrome(palindrome)
    print("\noutput:", serialize(ans, "string"))
