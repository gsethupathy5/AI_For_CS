# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfCuts(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numberOfCuts(n)
    print("\noutput:", serialize(ans, "integer"))
