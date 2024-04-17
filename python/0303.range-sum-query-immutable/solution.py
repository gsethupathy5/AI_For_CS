# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/range-sum-query-immutable/

from typing import *
from leetgo_py import *

# @lc code=begin

class NumArray:

    def __init__(self, nums: List[int]):
        

    def sumRange(self, left: int, right: int) -> int:
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    nums: List[int] = deserialize("List[int]", constructor_params[0])
    numsSize: int = deserialize("int", constructor_params[1])
    obj = NumArray(nums, numsSize)

    for i in range(1, len(ops)):
        match ops[i]:
            case "sumRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                ans = serialize(obj.sumRange(left, right))
                output.append(ans)

    print("\noutput:", join_array(output))
