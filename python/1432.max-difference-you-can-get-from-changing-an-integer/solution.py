# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxDiff(self, num: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().maxDiff(num)
    print("\noutput:", serialize(ans, "integer"))
