# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/recover-binary-search-tree/

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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    recoverTree(root)
    ans = root
    print("\noutput:", serialize(ans, "TreeNode"))
