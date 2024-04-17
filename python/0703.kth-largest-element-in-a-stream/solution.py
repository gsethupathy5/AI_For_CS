# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import *
from leetgo_py import *

# @lc code=begin

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        

    def add(self, val: int) -> int:
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    k: int = deserialize("int", constructor_params[0])
    nums: List[int] = deserialize("List[int]", constructor_params[1])
    numsSize: int = deserialize("int", constructor_params[2])
    obj = KthLargest(k, nums, numsSize)

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                ans = serialize(obj.add(val))
                output.append(ans)

    print("\noutput:", join_array(output))
