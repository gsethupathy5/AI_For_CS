# Created by asetti2002 at 2024/05/01 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/count-total-number-of-colored-cells/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * n - n + 1
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().coloredCells(n)
    print("\noutput:", serialize(ans, "long"))
