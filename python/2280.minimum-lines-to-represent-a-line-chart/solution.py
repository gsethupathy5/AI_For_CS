# Created by asetti2002 at 2024/05/01 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        return len(stockPrices) - 1
# @lc code=end

if __name__ == "__main__":
    stockPrices: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumLines(stockPrices)
    print("\noutput:", serialize(ans, "integer"))
