# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/detect-squares/

from typing import *
from leetgo_py import *

# @lc code=begin

class DetectSquares:

    def __init__(self):
        

    def add(self, point: List[int]) -> None:
        

    def count(self, point: List[int]) -> int:
        

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = DetectSquares()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                point: List[int] = deserialize("List[int]", method_params[0])
                obj.add(point)
                output.append("null")
            case "count":
                method_params = split_array(params[i])
                point: List[int] = deserialize("List[int]", method_params[0])
                ans = serialize(obj.count(point))
                output.append(ans)

    print("\noutput:", join_array(output))
