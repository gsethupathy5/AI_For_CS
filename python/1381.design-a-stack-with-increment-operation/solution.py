# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/design-a-stack-with-increment-operation/

from typing import *
from leetgo_py import *

# @lc code=begin

class CustomStack:

    def __init__(self, maxSize: int):
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def increment(self, k: int, val: int) -> None:
        

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    maxSize: int = deserialize("int", constructor_params[0])
    obj = CustomStack(maxSize)

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                x: int = deserialize("int", method_params[0])
                obj.push(x)
                output.append("null")
            case "pop":
                ans = serialize(obj.pop())
                output.append(ans)
            case "increment":
                method_params = split_array(params[i])
                k: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.increment(k, val)
                output.append("null")

    print("\noutput:", join_array(output))
