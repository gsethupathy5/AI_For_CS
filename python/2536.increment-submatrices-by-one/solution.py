# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/increment-submatrices-by-one/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().rangeAddQueries(n, queries)
    print("\noutput:", serialize(ans, "integer[][]"))
