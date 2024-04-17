# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/cycle-length-queries-in-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().cycleLengthQueries(n, queries)
    print("\noutput:", serialize(ans, "integer[]"))
