# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/most-profitable-path-in-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    bob: int = deserialize("int", read_line())
    amount: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mostProfitablePath(edges, bob, amount)
    print("\noutput:", serialize(ans, "integer"))
