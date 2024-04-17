# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/tallest-billboard/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    rods: List[int] = deserialize("List[int]", read_line())
    ans = Solution().tallestBillboard(rods)
    print("\noutput:", serialize(ans, "integer"))
