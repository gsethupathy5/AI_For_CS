# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/selling-pieces-of-wood/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    prices: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sellingWood(m, n, prices)
    print("\noutput:", serialize(ans, "long"))
