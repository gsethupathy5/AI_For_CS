# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/range-sum-query-2d-immutable/

from typing import *
from leetgo_py import *

# @lc code=begin

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    matrix: List[List[int]] = deserialize("List[List[int]]", constructor_params[0])
    matrixRowSize: int = deserialize("int", constructor_params[1])
    matrixColSize: int = deserialize("int", constructor_params[2])
    obj = NumMatrix(matrix, matrixRowSize, matrixColSize)

    for i in range(1, len(ops)):
        match ops[i]:
            case "sumRegion":
                method_params = split_array(params[i])
                row1: int = deserialize("int", method_params[0])
                col1: int = deserialize("int", method_params[1])
                row2: int = deserialize("int", method_params[2])
                col2: int = deserialize("int", method_params[3])
                ans = serialize(obj.sumRegion(row1, col1, row2, col2))
                output.append(ans)

    print("\noutput:", join_array(output))
