# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-search-tree-iterator/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        

    def next(self) -> int:
        

    def hasNext(self) -> bool:
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    root: TreeNode = deserialize("TreeNode", constructor_params[0])
    obj = BSTIterator(root)

    for i in range(1, len(ops)):
        match ops[i]:
            case "next":
                ans = serialize(obj.next())
                output.append(ans)
            case "hasNext":
                ans = serialize(obj.hasNext())
                output.append(ans)

    print("\noutput:", join_array(output))
