# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

from typing import *
from leetgo_py import *

# @lc code=begin

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        

    def getKthAncestor(self, node: int, k: int) -> int:
        

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    parent: List[int] = deserialize("List[int]", constructor_params[1])
    obj = TreeAncestor(n, parent)

    for i in range(1, len(ops)):
        match ops[i]:
            case "getKthAncestor":
                method_params = split_array(params[i])
                node: int = deserialize("int", method_params[0])
                k: int = deserialize("int", method_params[1])
                ans = serialize(obj.getKthAncestor(node, k))
                output.append(ans)

    print("\noutput:", join_array(output))
