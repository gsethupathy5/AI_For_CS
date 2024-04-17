# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    bloomDay: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minDays(bloomDay, m, k)
    print("\noutput:", serialize(ans, "integer"))
