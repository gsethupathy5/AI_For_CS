# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/range-frequency-queries/

from typing import *
from leetgo_py import *

# @lc code=begin

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        

    def query(self, left: int, right: int, value: int) -> int:
        

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    arr: List[int] = deserialize("List[int]", constructor_params[0])
    obj = RangeFreqQuery(arr)

    for i in range(1, len(ops)):
        match ops[i]:
            case "query":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                value: int = deserialize("int", method_params[2])
                ans = serialize(obj.query(left, right, value))
                output.append(ans)

    print("\noutput:", join_array(output))
