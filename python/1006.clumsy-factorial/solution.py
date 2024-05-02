# Created by asetti2002 at 2024/04/25 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/clumsy-factorial/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 6
        elif n == 4:
            return 7
        else:
            return n + 1 + ((n * (n - 1)) // (n - 2)) - (n - 3) * (n - 4) + self.clumsy(n - 4)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().clumsy(n)
    print("\noutput:", serialize(ans, "integer"))
