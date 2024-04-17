# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/building-boxes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumBoxes(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().minimumBoxes(n)
    print("\noutput:", serialize(ans, "integer"))
