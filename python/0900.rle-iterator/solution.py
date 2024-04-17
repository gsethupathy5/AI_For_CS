# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/rle-iterator/

from typing import *
from leetgo_py import *

# @lc code=begin

class RLEIterator:

    def __init__(self, encoding: List[int]):
        

    def next(self, n: int) -> int:
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    encoding: List[int] = deserialize("List[int]", constructor_params[0])
    obj = RLEIterator(encoding)

    for i in range(1, len(ops)):
        match ops[i]:
            case "next":
                method_params = split_array(params[i])
                n: int = deserialize("int", method_params[0])
                ans = serialize(obj.next(n))
                output.append(ans)

    print("\noutput:", join_array(output))
