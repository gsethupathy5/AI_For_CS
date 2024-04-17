# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-number-in-infinite-set/

from typing import *
from leetgo_py import *

# @lc code=begin

class SmallestInfiniteSet:

    def __init__(self):
        

    def popSmallest(self) -> int:
        

    def addBack(self, num: int) -> None:
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = SmallestInfiniteSet()

    for i in range(1, len(ops)):
        match ops[i]:
            case "popSmallest":
                ans = serialize(obj.popSmallest())
                output.append(ans)
            case "addBack":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addBack(num)
                output.append("null")

    print("\noutput:", join_array(output))
