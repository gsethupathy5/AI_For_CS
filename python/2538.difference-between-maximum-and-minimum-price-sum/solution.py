# Created by asetti2002 at 2024/05/01 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        return max(price) - min(price) + sum(price) - max(price) - sum(min(max(price), min(price), key=lambda x: sum(price[e] for e in edges if x in e)) * 2 - max(map(lambda x: sum(price[e] for e in edges if x in e), price) if price)}
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    price: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxOutput(n, edges, price)
    print("\noutput:", serialize(ans, "long"))
