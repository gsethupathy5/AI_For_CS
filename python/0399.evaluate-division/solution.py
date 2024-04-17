# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/evaluate-division/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

# @lc code=end

if __name__ == "__main__":
    equations: List[List[str]] = deserialize("List[List[str]]", read_line())
    values: List[float] = deserialize("List[float]", read_line())
    queries: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().calcEquation(equations, values, queries)
    print("\noutput:", serialize(ans, "double[]"))
