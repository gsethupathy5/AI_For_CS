# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        

# @lc code=end

if __name__ == "__main__":
    traversal: str = deserialize("str", read_line())
    ans = Solution().recoverFromPreorder(traversal)
    print("\noutput:", serialize(ans, "TreeNode"))