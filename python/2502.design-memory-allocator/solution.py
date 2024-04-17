# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/design-memory-allocator/

from typing import *
from leetgo_py import *

# @lc code=begin

class Allocator:

    def __init__(self, n: int):
        

    def allocate(self, size: int, mID: int) -> int:
        

    def free(self, mID: int) -> int:
        

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    obj = Allocator(n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "allocate":
                method_params = split_array(params[i])
                size: int = deserialize("int", method_params[0])
                mID: int = deserialize("int", method_params[1])
                ans = serialize(obj.allocate(size, mID))
                output.append(ans)
            case "free":
                method_params = split_array(params[i])
                mID: int = deserialize("int", method_params[0])
                ans = serialize(obj.free(mID))
                output.append(ans)

    print("\noutput:", join_array(output))
