# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findSmallestSetOfVertices(n, edges)
    print("\noutput:", serialize(ans, "integer[]"))
