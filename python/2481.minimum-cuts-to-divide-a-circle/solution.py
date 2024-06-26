# Created by asetti2002 at 2024/05/01 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return n
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numberOfCuts(n)
    print("\noutput:", serialize(ans, "integer"))
