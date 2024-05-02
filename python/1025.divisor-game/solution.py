# Created by asetti2002 at 2024/04/25 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/divisor-game/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().divisorGame(n)
    print("\noutput:", serialize(ans, "boolean"))
