# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/ipo/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    w: int = deserialize("int", read_line())
    profits: List[int] = deserialize("List[int]", read_line())
    capital: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMaximizedCapital(k, w, profits, capital)
    print("\noutput:", serialize(ans, "integer"))
