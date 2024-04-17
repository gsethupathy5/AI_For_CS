# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/design-bitset/

from typing import *
from leetgo_py import *

# @lc code=begin

class Bitset:

    def __init__(self, size: int):
        

    def fix(self, idx: int) -> None:
        

    def unfix(self, idx: int) -> None:
        

    def flip(self) -> None:
        

    def all(self) -> bool:
        

    def one(self) -> bool:
        

    def count(self) -> int:
        

    def toString(self) -> str:
        

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    size: int = deserialize("int", constructor_params[0])
    obj = Bitset(size)

    for i in range(1, len(ops)):
        match ops[i]:
            case "fix":
                method_params = split_array(params[i])
                idx: int = deserialize("int", method_params[0])
                obj.fix(idx)
                output.append("null")
            case "unfix":
                method_params = split_array(params[i])
                idx: int = deserialize("int", method_params[0])
                obj.unfix(idx)
                output.append("null")
            case "flip":
                obj.flip()
                output.append("null")
            case "all":
                ans = serialize(obj.all())
                output.append(ans)
            case "one":
                ans = serialize(obj.one())
                output.append(ans)
            case "count":
                ans = serialize(obj.count())
                output.append(ans)
            case "toString":
                ans = serialize(obj.toString())
                output.append(ans)

    print("\noutput:", join_array(output))
