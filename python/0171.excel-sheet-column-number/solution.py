# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/excel-sheet-column-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    columnTitle: str = deserialize("str", read_line())
    ans = Solution().titleToNumber(columnTitle)
    print("\noutput:", serialize(ans, "integer"))
