# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/range-product-queries-of-powers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().productQueries(n, queries)
    print("\noutput:", serialize(ans, "integer[]"))
