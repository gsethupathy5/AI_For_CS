# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/design-circular-deque/

from typing import *
from leetgo_py import *

# @lc code=begin

class MyCircularDeque:

    def __init__(self, k: int):
        

    def insertFront(self, value: int) -> bool:
        

    def insertLast(self, value: int) -> bool:
        

    def deleteFront(self) -> bool:
        

    def deleteLast(self) -> bool:
        

    def getFront(self) -> int:
        

    def getRear(self) -> int:
        

    def isEmpty(self) -> bool:
        

    def isFull(self) -> bool:
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    k: int = deserialize("int", constructor_params[0])
    obj = MyCircularDeque(k)

    for i in range(1, len(ops)):
        match ops[i]:
            case "insertFront":
                method_params = split_array(params[i])
                value: int = deserialize("int", method_params[0])
                ans = serialize(obj.insertFront(value))
                output.append(ans)
            case "insertLast":
                method_params = split_array(params[i])
                value: int = deserialize("int", method_params[0])
                ans = serialize(obj.insertLast(value))
                output.append(ans)
            case "deleteFront":
                ans = serialize(obj.deleteFront())
                output.append(ans)
            case "deleteLast":
                ans = serialize(obj.deleteLast())
                output.append(ans)
            case "getFront":
                ans = serialize(obj.getFront())
                output.append(ans)
            case "getRear":
                ans = serialize(obj.getRear())
                output.append(ans)
            case "isEmpty":
                ans = serialize(obj.isEmpty())
                output.append(ans)
            case "isFull":
                ans = serialize(obj.isFull())
                output.append(ans)

    print("\noutput:", join_array(output))
