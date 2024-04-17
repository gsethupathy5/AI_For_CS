# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    allowed: str = deserialize("str", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().countConsistentStrings(allowed, words)
    print("\noutput:", serialize(ans, "integer"))
