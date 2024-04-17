# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-genetic-difference-query/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    parents: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxGeneticDifference(parents, queries)
    print("\noutput:", serialize(ans, "integer[]"))
