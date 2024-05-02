# Created by asetti2002 at 2024/05/01 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def monkeyMove(self, n: int) -> int:
        return (2 ** (n - 1) * n - n) % (10**9 + 7)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().monkeyMove(n)
    print("\noutput:", serialize(ans, "integer"))
