# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-lines-to-write-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    widths: List[int] = deserialize("List[int]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().numberOfLines(widths, s)
    print("\noutput:", serialize(ans, "integer[]"))
