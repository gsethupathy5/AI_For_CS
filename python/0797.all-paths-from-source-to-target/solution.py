# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().allPathsSourceTarget(graph)
    print("\noutput:", serialize(ans, "integer[][]"))
