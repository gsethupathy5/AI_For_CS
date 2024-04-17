# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-paths/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().uniquePaths(m, n)
    print("\noutput:", serialize(ans, "integer"))
