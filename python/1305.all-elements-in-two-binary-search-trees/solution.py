# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().getAllElements(root1, root2)
    print("\noutput:", serialize(ans, "integer[]"))
