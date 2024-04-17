# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

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
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    startValue: int = deserialize("int", read_line())
    destValue: int = deserialize("int", read_line())
    ans = Solution().getDirections(root, startValue, destValue)
    print("\noutput:", serialize(ans, "string"))
