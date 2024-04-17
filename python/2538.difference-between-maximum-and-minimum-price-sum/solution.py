# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    price: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxOutput(n, edges, price)
    print("\noutput:", serialize(ans, "long"))
