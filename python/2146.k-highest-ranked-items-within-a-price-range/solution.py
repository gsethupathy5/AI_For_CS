# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    pricing: List[int] = deserialize("List[int]", read_line())
    start: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().highestRankedKItems(grid, pricing, start, k)
    print("\noutput:", serialize(ans, "integer[][]"))
