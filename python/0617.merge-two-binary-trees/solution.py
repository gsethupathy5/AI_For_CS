# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/merge-two-binary-trees/

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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        

# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().mergeTrees(root1, root2)
    print("\noutput:", serialize(ans, "TreeNode"))
