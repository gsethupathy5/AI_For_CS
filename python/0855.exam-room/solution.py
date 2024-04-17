# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/exam-room/

from typing import *
from leetgo_py import *

# @lc code=begin

class ExamRoom:

    def __init__(self, n: int):
        

    def seat(self) -> int:
        

    def leave(self, p: int) -> None:
        

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    obj = ExamRoom(n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "seat":
                ans = serialize(obj.seat())
                output.append(ans)
            case "leave":
                method_params = split_array(params[i])
                p: int = deserialize("int", method_params[0])
                obj.leave(p)
                output.append("null")

    print("\noutput:", join_array(output))
