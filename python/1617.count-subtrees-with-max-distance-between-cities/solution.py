# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countSubgraphsForEachDiameter(n, edges)
    print("\noutput:", serialize(ans, "integer[]"))
