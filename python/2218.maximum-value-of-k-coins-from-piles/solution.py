# Created by asetti2002 at 2024/04/25 20:24
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        piles = sorted([coin for pile in piles for coin in pile], reverse=True)
        return sum(piles[:k])
# @lc code=end

if __name__ == "__main__":
    piles: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxValueOfCoins(piles, k)
    print("\noutput:", serialize(ans, "integer"))
