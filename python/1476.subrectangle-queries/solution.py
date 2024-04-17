# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/subrectangle-queries/

from typing import *
from leetgo_py import *

# @lc code=begin

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        

    def getValue(self, row: int, col: int) -> int:
        

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    rectangle: List[List[int]] = deserialize("List[List[int]]", constructor_params[0])
    obj = SubrectangleQueries(rectangle)

    for i in range(1, len(ops)):
        match ops[i]:
            case "updateSubrectangle":
                method_params = split_array(params[i])
                row1: int = deserialize("int", method_params[0])
                col1: int = deserialize("int", method_params[1])
                row2: int = deserialize("int", method_params[2])
                col2: int = deserialize("int", method_params[3])
                newValue: int = deserialize("int", method_params[4])
                obj.updateSubrectangle(row1, col1, row2, col2, newValue)
                output.append("null")
            case "getValue":
                method_params = split_array(params[i])
                row: int = deserialize("int", method_params[0])
                col: int = deserialize("int", method_params[1])
                ans = serialize(obj.getValue(row, col))
                output.append(ans)

    print("\noutput:", join_array(output))
