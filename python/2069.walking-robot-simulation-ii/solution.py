# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/walking-robot-simulation-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Robot:

    def __init__(self, width: int, height: int):
        

    def step(self, num: int) -> None:
        

    def getPos(self) -> List[int]:
        

    def getDir(self) -> str:
        

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    width: int = deserialize("int", constructor_params[0])
    height: int = deserialize("int", constructor_params[1])
    obj = Robot(width, height)

    for i in range(1, len(ops)):
        match ops[i]:
            case "step":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.step(num)
                output.append("null")
            case "getPos":
                ans = serialize(obj.getPos())
                output.append(ans)
            case "getDir":
                ans = serialize(obj.getDir())
                output.append(ans)

    print("\noutput:", join_array(output))
