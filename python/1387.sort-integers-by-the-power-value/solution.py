# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-integers-by-the-power-value/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    lo: int = deserialize("int", read_line())
    hi: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getKth(lo, hi, k)
    print("\noutput:", serialize(ans, "integer"))
