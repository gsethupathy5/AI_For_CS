# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/seat-reservation-manager/

from typing import *
from leetgo_py import *

# @lc code=begin

class SeatManager:

    def __init__(self, n: int):
        

    def reserve(self) -> int:
        

    def unreserve(self, seatNumber: int) -> None:
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    obj = SeatManager(n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "reserve":
                ans = serialize(obj.reserve())
                output.append(ans)
            case "unreserve":
                method_params = split_array(params[i])
                seatNumber: int = deserialize("int", method_params[0])
                obj.unreserve(seatNumber)
                output.append("null")

    print("\noutput:", join_array(output))
