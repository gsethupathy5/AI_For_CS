# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/range-module/

from typing import *
from leetgo_py import *

# @lc code=begin

class RangeModule:

    def __init__(self):
        

    def addRange(self, left: int, right: int) -> None:
        

    def queryRange(self, left: int, right: int) -> bool:
        

    def removeRange(self, left: int, right: int) -> None:
        

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = RangeModule()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                obj.addRange(left, right)
                output.append("null")
            case "queryRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                ans = serialize(obj.queryRange(left, right))
                output.append(ans)
            case "removeRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                obj.removeRange(left, right)
                output.append("null")

    print("\noutput:", join_array(output))
