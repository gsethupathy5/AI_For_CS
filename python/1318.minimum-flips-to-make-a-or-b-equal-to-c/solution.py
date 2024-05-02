# Created by asetti2002 at 2024/04/25 20:30
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count('1') + bin(c).count('1') - bin(a).count('1') - bin(b).count('1')
# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().minFlips(a, b, c)
    print("\noutput:", serialize(ans, "integer"))
