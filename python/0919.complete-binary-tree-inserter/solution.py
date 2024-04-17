# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/complete-binary-tree-inserter/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        

    def insert(self, val: int) -> int:
        

    def get_root(self) -> Optional[TreeNode]:
        

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    root: TreeNode = deserialize("TreeNode", constructor_params[0])
    obj = CBTInserter(root)

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                ans = serialize(obj.insert(val))
                output.append(ans)
            case "get_root":
                ans = serialize(obj.get_root())
                output.append(ans)

    print("\noutput:", join_array(output))
