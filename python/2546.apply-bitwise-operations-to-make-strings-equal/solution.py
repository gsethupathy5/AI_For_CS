# Created by asetti2002 at 2024/05/01 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return sum(int(c) for c in s) % 2 == sum(int(c) for c in target) % 2
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().makeStringsEqual(s, target)
    print("\noutput:", serialize(ans, "boolean"))
