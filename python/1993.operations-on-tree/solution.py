# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/operations-on-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class LockingTree:

    def __init__(self, parent: List[int]):
        

    def lock(self, num: int, user: int) -> bool:
        

    def unlock(self, num: int, user: int) -> bool:
        

    def upgrade(self, num: int, user: int) -> bool:
        

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    parent: List[int] = deserialize("List[int]", constructor_params[0])
    obj = LockingTree(parent)

    for i in range(1, len(ops)):
        match ops[i]:
            case "lock":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                user: int = deserialize("int", method_params[1])
                ans = serialize(obj.lock(num, user))
                output.append(ans)
            case "unlock":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                user: int = deserialize("int", method_params[1])
                ans = serialize(obj.unlock(num, user))
                output.append(ans)
            case "upgrade":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                user: int = deserialize("int", method_params[1])
                ans = serialize(obj.upgrade(num, user))
                output.append(ans)

    print("\noutput:", join_array(output))
