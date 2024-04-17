# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/zigzag-conversion/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    numRows: int = deserialize("int", read_line())
    ans = Solution().convert(s, numRows)
    print("\noutput:", serialize(ans, "string"))
