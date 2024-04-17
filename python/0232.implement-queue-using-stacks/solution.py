# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/implement-queue-using-stacks/

from typing import *
from leetgo_py import *

# @lc code=begin

class MyQueue:

    def __init__(self):
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def peek(self) -> int:
        

    def empty(self) -> bool:
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyQueue()

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
            case "peek":
                ans = serialize(obj.peek())
                output.append(ans)
            case "empty":
                ans = serialize(obj.empty())
                output.append(ans)

    print("\noutput:", join_array(output))
