# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/my-calendar-i/

from typing import *
from leetgo_py import *

# @lc code=begin

class MyCalendar:

    def __init__(self):
        

    def book(self, start: int, end: int) -> bool:
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyCalendar()

    for i in range(1, len(ops)):
        match ops[i]:
            case "book":
                method_params = split_array(params[i])
                start: int = deserialize("int", method_params[0])
                end: int = deserialize("int", method_params[1])
                ans = serialize(obj.book(start, end))
                output.append(ans)

    print("\noutput:", join_array(output))
