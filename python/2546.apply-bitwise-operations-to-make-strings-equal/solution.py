# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().makeStringsEqual(s, target)
    print("\noutput:", serialize(ans, "boolean"))
