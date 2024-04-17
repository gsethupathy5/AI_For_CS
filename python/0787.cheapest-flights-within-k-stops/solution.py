# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    flights: List[List[int]] = deserialize("List[List[int]]", read_line())
    src: int = deserialize("int", read_line())
    dst: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findCheapestPrice(n, flights, src, dst, k)
    print("\noutput:", serialize(ans, "integer"))
