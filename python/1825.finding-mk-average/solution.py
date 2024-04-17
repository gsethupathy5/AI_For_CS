# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/finding-mk-average/

from typing import *
from leetgo_py import *

# @lc code=begin

class MKAverage:

    def __init__(self, m: int, k: int):
        

    def addElement(self, num: int) -> None:
        

    def calculateMKAverage(self) -> int:
        

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    m: int = deserialize("int", constructor_params[0])
    k: int = deserialize("int", constructor_params[1])
    obj = MKAverage(m, k)

    for i in range(1, len(ops)):
        match ops[i]:
            case "addElement":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addElement(num)
                output.append("null")
            case "calculateMKAverage":
                ans = serialize(obj.calculateMKAverage())
                output.append(ans)

    print("\noutput:", join_array(output))
