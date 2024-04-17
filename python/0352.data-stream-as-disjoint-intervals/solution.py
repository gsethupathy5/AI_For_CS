# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin

class SummaryRanges:

    def __init__(self):
        

    def addNum(self, value: int) -> None:
        

    def getIntervals(self) -> List[List[int]]:
        

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = SummaryRanges()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addNum":
                method_params = split_array(params[i])
                value: int = deserialize("int", method_params[0])
                obj.addNum(value)
                output.append("null")
            case "getIntervals":
                ans = serialize(obj.getIntervals())
                output.append(ans)

    print("\noutput:", join_array(output))
