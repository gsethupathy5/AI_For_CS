# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/profitable-schemes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    minProfit: int = deserialize("int", read_line())
    group: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().profitableSchemes(n, minProfit, group, profit)
    print("\noutput:", serialize(ans, "integer"))
