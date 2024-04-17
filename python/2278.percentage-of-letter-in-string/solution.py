# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/percentage-of-letter-in-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    letter: str = deserialize("str", read_line())
    ans = Solution().percentageLetter(s, letter)
    print("\noutput:", serialize(ans, "integer"))
