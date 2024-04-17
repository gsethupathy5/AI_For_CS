# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    quadTree1: List[List[int]] = deserialize("List[List[int]]", read_line())
    quadTree2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().intersect(quadTree1, quadTree2)
    print("\noutput:", serialize(ans, "integer[][]"))
