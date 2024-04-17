# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/fancy-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Fancy:

    def __init__(self):
        

    def append(self, val: int) -> None:
        

    def addAll(self, inc: int) -> None:
        

    def multAll(self, m: int) -> None:
        

    def getIndex(self, idx: int) -> int:
        

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Fancy()

    for i in range(1, len(ops)):
        match ops[i]:
            case "append":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.append(val)
                output.append("null")
            case "addAll":
                method_params = split_array(params[i])
                inc: int = deserialize("int", method_params[0])
                obj.addAll(inc)
                output.append("null")
            case "multAll":
                method_params = split_array(params[i])
                m: int = deserialize("int", method_params[0])
                obj.multAll(m)
                output.append("null")
            case "getIndex":
                method_params = split_array(params[i])
                idx: int = deserialize("int", method_params[0])
                ans = serialize(obj.getIndex(idx))
                output.append(ans)

    print("\noutput:", join_array(output))
