# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().levelOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
