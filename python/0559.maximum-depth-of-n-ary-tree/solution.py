# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().maxDepth(root)
    print("\noutput:", serialize(ans, "integer"))
