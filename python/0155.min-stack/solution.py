# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/min-stack/

from typing import *
from leetgo_py import *

# @lc code=begin

class MinStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MinStack()

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.push(val)
                output.append("null")
            case "pop":
                obj.pop()
                output.append("null")
            case "top":
                ans = serialize(obj.top())
                output.append(ans)
            case "getMin":
                ans = serialize(obj.getMin())
                output.append(ans)

    print("\noutput:", join_array(output))
