# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/prison-cells-after-n-days/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    cells: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().prisonAfterNDays(cells, n)
    print("\noutput:", serialize(ans, "integer[]"))
