# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
