# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minDays(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().minDays(n)
    print("\noutput:", serialize(ans, "integer"))