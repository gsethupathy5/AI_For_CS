# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/clone-graph/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().cloneGraph(edges)
    print("\noutput:", serialize(ans, "boolean"))
