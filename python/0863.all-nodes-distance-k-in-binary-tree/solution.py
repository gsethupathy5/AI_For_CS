# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    target: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().distanceK(root, target, k)
    print("\noutput:", serialize(ans, "integer[]"))
