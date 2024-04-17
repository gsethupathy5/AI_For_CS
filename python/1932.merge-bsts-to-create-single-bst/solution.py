# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/merge-bsts-to-create-single-bst/

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
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    trees: List[TreeNode] = deserialize("List[TreeNode]", read_line())
    ans = Solution().canMerge(trees)
    print("\noutput:", serialize(ans, "TreeNode"))
