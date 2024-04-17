# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/dinner-plate-stacks/

from typing import *
from leetgo_py import *

# @lc code=begin

class DinnerPlates:

    def __init__(self, capacity: int):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> int:
        

    def popAtStack(self, index: int) -> int:
        

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    capacity: int = deserialize("int", constructor_params[0])
    obj = DinnerPlates(capacity)

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.push(val)
                output.append("null")
            case "pop":
                ans = serialize(obj.pop())
                output.append(ans)
            case "popAtStack":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                ans = serialize(obj.popAtStack(index))
                output.append(ans)

    print("\noutput:", join_array(output))
