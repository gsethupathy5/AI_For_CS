# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/design-circular-queue/

from typing import *
from leetgo_py import *

# @lc code=begin

class MyCircularQueue:

    def __init__(self, k: int):
        

    def enQueue(self, value: int) -> bool:
        

    def deQueue(self) -> bool:
        

    def Front(self) -> int:
        

    def Rear(self) -> int:
        

    def isEmpty(self) -> bool:
        

    def isFull(self) -> bool:
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    k: int = deserialize("int", constructor_params[0])
    obj = MyCircularQueue(k)

    for i in range(1, len(ops)):
        match ops[i]:
            case "enQueue":
                method_params = split_array(params[i])
                value: int = deserialize("int", method_params[0])
                ans = serialize(obj.enQueue(value))
                output.append(ans)
            case "deQueue":
                ans = serialize(obj.deQueue())
                output.append(ans)
            case "Front":
                ans = serialize(obj.Front())
                output.append(ans)
            case "Rear":
                ans = serialize(obj.Rear())
                output.append(ans)
            case "isEmpty":
                ans = serialize(obj.isEmpty())
                output.append(ans)
            case "isFull":
                ans = serialize(obj.isFull())
                output.append(ans)

    print("\noutput:", join_array(output))
