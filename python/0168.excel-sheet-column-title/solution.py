# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/excel-sheet-column-title/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    columnNumber: int = deserialize("int", read_line())
    ans = Solution().convertToTitle(columnNumber)
    print("\noutput:", serialize(ans, "string"))
