# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-integers-in-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin

class CountIntervals:

    def __init__(self):
        

    def add(self, left: int, right: int) -> None:
        

    def count(self) -> int:
        

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = CountIntervals()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                obj.add(left, right)
                output.append("null")
            case "count":
                ans = serialize(obj.count())
                output.append(ans)

    print("\noutput:", join_array(output))
