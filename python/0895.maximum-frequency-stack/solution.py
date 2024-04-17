# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-frequency-stack/

from typing import *
from leetgo_py import *

# @lc code=begin

class FreqStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> int:
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = FreqStack()

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

    print("\noutput:", join_array(output))
