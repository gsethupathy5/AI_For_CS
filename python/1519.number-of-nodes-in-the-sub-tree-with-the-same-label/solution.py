# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    labels: str = deserialize("str", read_line())
    ans = Solution().countSubTrees(n, edges, labels)
    print("\noutput:", serialize(ans, "integer[]"))
