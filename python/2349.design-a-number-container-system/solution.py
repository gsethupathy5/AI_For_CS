# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/design-a-number-container-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class NumberContainers:

    def __init__(self):
        

    def change(self, index: int, number: int) -> None:
        

    def find(self, number: int) -> int:
        

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = NumberContainers()

    for i in range(1, len(ops)):
        match ops[i]:
            case "change":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                number: int = deserialize("int", method_params[1])
                obj.change(index, number)
                output.append("null")
            case "find":
                method_params = split_array(params[i])
                number: int = deserialize("int", method_params[0])
                ans = serialize(obj.find(number))
                output.append(ans)

    print("\noutput:", join_array(output))
