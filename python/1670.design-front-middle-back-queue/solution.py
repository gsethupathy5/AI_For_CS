# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/design-front-middle-back-queue/

from typing import *
from leetgo_py import *

# @lc code=begin

class FrontMiddleBackQueue:

    def __init__(self):
        

    def pushFront(self, val: int) -> None:
        

    def pushMiddle(self, val: int) -> None:
        

    def pushBack(self, val: int) -> None:
        

    def popFront(self) -> int:
        

    def popMiddle(self) -> int:
        

    def popBack(self) -> int:
        

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = FrontMiddleBackQueue()

    for i in range(1, len(ops)):
        match ops[i]:
            case "pushFront":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushFront(val)
                output.append("null")
            case "pushMiddle":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushMiddle(val)
                output.append("null")
            case "pushBack":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushBack(val)
                output.append("null")
            case "popFront":
                ans = serialize(obj.popFront())
                output.append(ans)
            case "popMiddle":
                ans = serialize(obj.popMiddle())
                output.append(ans)
            case "popBack":
                ans = serialize(obj.popBack())
                output.append(ans)

    print("\noutput:", join_array(output))
