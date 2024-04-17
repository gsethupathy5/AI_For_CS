# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/booking-concert-tickets-in-groups/

from typing import *
from leetgo_py import *

# @lc code=begin

class BookMyShow:

    def __init__(self, n: int, m: int):
        

    def gather(self, k: int, maxRow: int) -> List[int]:
        

    def scatter(self, k: int, maxRow: int) -> bool:
        

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    m: int = deserialize("int", constructor_params[1])
    obj = BookMyShow(n, m)

    for i in range(1, len(ops)):
        match ops[i]:
            case "gather":
                method_params = split_array(params[i])
                k: int = deserialize("int", method_params[0])
                maxRow: int = deserialize("int", method_params[1])
                ans = serialize(obj.gather(k, maxRow))
                output.append(ans)
            case "scatter":
                method_params = split_array(params[i])
                k: int = deserialize("int", method_params[0])
                maxRow: int = deserialize("int", method_params[1])
                ans = serialize(obj.scatter(k, maxRow))
                output.append(ans)

    print("\noutput:", join_array(output))
